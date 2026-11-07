# Section 4: Kubernetes Integration (5%)

**Last reviewed:** 2026-11-07

Two objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) (checked 2026-11-07): deploy the NVIDIA Network Operator to manage RDMA interfaces and InfiniBand networks within Kubernetes clusters, and verify its functionality. This was the gap the old guide listed as "not covered". The manifests below come from NVIDIA's Network Operator deployment guide for v25.7.0 and were not run (no Kubernetes cluster with NVIDIA NICs was available).

**[📖 NVIDIA Network Operator deployment guide (v25.7.0)](https://docs.nvidia.com/networking/display/kubernetes2570/deployment-guide-kubernetes.html)** - Prerequisites, Helm install, NicClusterPolicy examples

## What the Network Operator is for

Kubernetes schedules pods onto nodes but knows nothing about RDMA devices or InfiniBand networks. The operator installs and manages the pieces that make them usable: the driver stack (DOCA-OFED), the device plugin that exposes RDMA devices to pods as schedulable resources, and the secondary network plumbing. NVIDIA's Spectrum-X page describes the operator as discovering the NICs, configuring rails and exposing them to pods as schedulable resources. The operator is configured through a custom resource, `NicClusterPolicy`.

## Deploy

Prerequisites from the guide: `kubectl` and `helm` on a client, a container engine such as CRI-O or containerd on the nodes, a privileged label on the operator namespace if Pod Security Admission is enforced, and Node Feature Discovery (NFD). The operator deploys NFD by default; if NFD already runs in the cluster, set `nfd.enabled=false`.

```
# Not run: from the NVIDIA guide
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
helm install network-operator nvidia/network-operator \
  -n nvidia-network-operator --create-namespace \
  --version v25.7.0 --wait
```

For custom settings: `helm show values nvidia/network-operator --version v25.7.0 > values.yaml`, edit, and install with `-f ./values.yaml`.

Then a `NicClusterPolicy` enables components. The guide's RDMA shared device plugin example (condensed) is:

```yaml
# Not run: condensed from the NVIDIA guide; replace ens1f0 with your node's netdev name
apiVersion: mellanox.com/v1alpha1
kind: NicClusterPolicy
metadata:
  name: nic-cluster-policy
spec:
  ofedDriver:
    image: doca-driver
    repository: nvcr.io/nvidia/mellanox
    version: doca3.1.0-25.07-0.9.7.0-0
  rdmaSharedDevicePlugin:
    image: k8s-rdma-shared-dev-plugin
    repository: nvcr.io/nvidia/mellanox
    version: network-operator-v25.7.0
    config: |
      {"configList": [{"resourceName": "rdma_shared_device_a",
                       "rdmaHcaMax": 63,
                       "selectors": {"ifNames": ["ens1f0"]}}]}
```

Reading it: `ofedDriver` deploys the DOCA-OFED driver container; `rdmaSharedDevicePlugin` advertises a resource called `rdma_shared_device_a` (up to 63 pods can share the device, `rdmaHcaMax`) mapped to the named netdev. One policy can define several resources, each mapped to different interfaces. Version differences matter: the v25.4.0 release notes say the operator no longer creates the NicClusterPolicy by default and deploys only the RDMA shared device plugin by default, and older guides used different image repositories. The guide says to change interface names to match your nodes.

- **Network Operator** - the NVIDIA Kubernetes operator that deploys and manages networking drivers, RDMA device plugins and secondary networks for NVIDIA NICs.
- **NicClusterPolicy** - the custom resource that tells the Network Operator which components to deploy (OFED driver, RDMA shared device plugin and others).
- **RDMA shared device plugin** - a Kubernetes device plugin that exposes RDMA-capable devices to pods as a named, shareable resource.
- **Node Feature Discovery (NFD)** - a Kubernetes add-on that labels nodes with hardware features; the Network Operator requires it and deploys it by default.

## Verify

The guide's own verification: `kubectl -n nvidia-network-operator get pods` after the chart install, which should show the operator and the components the policy enabled, running. Pods that use the devices request the resource in `requests` and `limits`, for example `rdma/rdma_shared_device_a: 1`; the guide's IPoIB test pod has a typo (`edma/` in `limits`), so the name in `requests` and `limits` must match exactly or the pod will not schedule. The guide I fetched does not describe an `ib_write_bw` or `ibv_devinfo` check; for a functional test the usual approach is to run those tools inside two RDMA pods (see the commands in the troubleshooting note), which is my suggestion and not from this page.

## Check yourself against the objectives

List the prerequisites; write the Helm install; say what a NicClusterPolicy with `ofedDriver` and `rdmaSharedDevicePlugin` produces; and describe how you would confirm pods can request RDMA devices. Questions are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
