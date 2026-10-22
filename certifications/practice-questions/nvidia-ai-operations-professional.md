---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA Certified Professional - AI Operations (NCP-AIO) - Practice Questions

30 questions for NCP-AIO prep, evenly weighted across MLOps and model lifecycle, deployment and serving, GPU monitoring with DCGM, fleet management, and incident response (20% each).

> **Cert page:** [exams/nvidia/ai-operations-professional/](../nvidia/ai-operations-professional/README.md)

---

### Question 1
**Scenario:** A model in production must be traceable back to the exact code, data, and hyperparameters that produced it.

A. The deployment date plus the commit hash of the serving repository, which together identify which release was running then
B. A model registry entry linking the artifact, training run, dataset version, and image digest, written automatically at training time
C. A note in the wiki
D. The filename

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lineage is what makes rollback and incident investigation possible, and it must be captured automatically at training time rather than reconstructed later. Pinning the container image by digest rather than tag closes the last mutable link in the chain.
</details>

---

### Question 2
**Scenario:** Triton must serve two model versions simultaneously so traffic can be shifted gradually.

A. Two separate Triton servers on different ports, each holding one model version, with clients choosing a port by hand
B. A model repository holding the versions with a version policy, fronted by traffic splitting
C. Restart with the new version
D. Only the latest version can be served

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Triton's model repository supports multiple versions per model with a configurable version policy, so both can be loaded at once. Combined with a router or service mesh doing the split, this gives canary deployment without duplicating the serving infrastructure.
</details>

---

### Question 3
**Scenario:** DCGM should detect a degrading GPU before it fails a production job.

A. Run scheduled DCGM diagnostics and alert on health checks, XID errors, throttling, and remapped rows
B. Monitor CPU temperature and load only, since GPU faults show up first in host metrics
C. Check quarterly
D. Wait for job failures

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DCGM exposes health watches and a diagnostic suite at several levels, and XID error codes identify specific fault classes. Proactive detection lets you drain the node during a maintenance window instead of losing a multi-day training run.
</details>

---

### Question 4
**Scenario:** An inference service must meet a p99 latency SLO under variable load.

A. Use a larger model, because added capacity per request reduces tail latency under any load pattern
B. Increase batch size indefinitely so that GPU utilization stays high and each request waits less on average
C. Size the fleet for average load plus a ten percent margin, and read mean latency to confirm it holds
D. Set the SLO, measure p99, autoscale on queue or latency, and reserve tail headroom

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Averages hide the tail that users actually experience, and larger batches trade latency for throughput, which pushes p99 the wrong way. Scaling on queue depth or latency responds faster than CPU or GPU utilization for serving workloads.
</details>

---

### Question 5
**Scenario:** Model accuracy in production degrades although the model file has not changed.

A. The image is corrupt, since each restart overwrites the weights on disk
B. The network is slow
C. Data or concept drift: monitor input distributions and outcomes, and trigger retraining
D. The GPU is broken

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The world moves even when the artifact does not. Monitoring input feature distributions catches data drift, and tracking realized outcomes against predictions catches concept drift. Without both, the first signal is a business metric moving months later.
</details>

---

### Question 6
**Scenario:** Driver versions have diverged across a 200-node fleet.

A. Manage drivers declaratively (GPU Operator or config management), enforce a version policy, roll in waves
B. Ignore the divergence
C. Reinstall the operating system on every node, and install whatever driver release the package repository currently offers
D. Fix them one at a time by hand, logging into each node and updating the driver whenever spare capacity is free to do so

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Divergence produces failures that reproduce on some nodes and not others, which is the most expensive kind to debug. Declarative management makes the fleet converge and makes drift visible. Wave-based rollout limits the blast radius of a bad driver.
</details>

---

### Question 7
**Scenario:** A CI pipeline for models should gate promotion to production.

A. Automated tests: data validation, reproducibility, an evaluation threshold, and a canary
B. Test in production
C. Manual approval by one senior engineer only, who reads the training log and signs off before every release
D. Deploy on merge with no checks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The distinctive part of ML CI is that the artifact depends on data, so data validation and an evaluation gate sit alongside ordinary code tests. Manual approval without evidence is a rubber stamp, and the canary catches what offline evaluation cannot.
</details>

---

### Question 8
**Scenario:** An incident occurs: inference errors spike at 03:00.

A. Follow the incident process: assess impact against the SLO, roll back to last good version, then find root cause
B. Wait for business hours
C. Restart every serving pod and node at once, since a restart clears whatever state caused the spike overnight and gives a clean start
D. Retrain the model on the latest data right away, then redeploy it, since errors this sudden mean the model has gone stale

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Mitigation precedes diagnosis: the fastest path back to a working service is usually rollback, and root cause analysis is done after users are safe. Retraining during an incident is the slowest possible response and often is not the cause.
</details>

---

### Question 9
**Scenario:** GPU utilization on the serving fleet averages 20%.

A. Leave it, because headroom this large guarantees the p99 target holds and avoids any scale-up delay during traffic peaks
B. Consolidate with MIG or multi-model serving, then right-size and autoscale
C. Increase the model size so that each request keeps the GPU busier, which raises utilization
D. Add more GPUs to the fleet so that the same load is spread across even more devices

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Persistent low utilization is money spent on idle silicon. MIG or Triton's concurrent model execution packs several models onto one GPU, and scaling policies release capacity off-peak. Keep enough headroom for the tail, but 20% average is far past that.
</details>

---

### Question 10
**Scenario:** Which metric best indicates that an inference server is saturated?

A. GPU temperature, since a saturated server runs hot and thermal readings rise before any request is delayed
B. Model file size
C. Queue delay and its effect on end-to-end latency
D. Disk usage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Triton reports queue duration separately from compute duration, which cleanly distinguishes "the model is slow" from "there is more work arriving than capacity to do it." Those two lead to different fixes: optimize the model, or add replicas.
</details>

---

### Question 11
**Scenario:** A disaster recovery plan is needed for an inference service in one region.

A. A written runbook reviewed once a year and stored with the service, assumed to work when the primary region fails
B. A second region with replicated registry and tested deployment automation, plus a rehearsed failover
C. Backups only
D. Rely on the cloud provider

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DR is only real if it has been exercised: an untested runbook reliably fails on a dependency nobody remembered, such as the registry, secrets, or DNS. Model artifacts and the deployment pipeline both need to exist in the second region before the incident.
</details>

---

### Question 12
**Scenario:** Compliance requires knowing which model version produced a given prediction six months ago.

A. Store the predictions only, with a timestamp but without recording which model produced each one
B. Rely on the deployment history, which lists every model version and the dates it was live in production
C. Log model name, version, and input and output IDs per inference, retained per policy
D. Nothing is needed, because auditors accept the current model's documentation for older predictions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Correlating a prediction to a version requires the version to be recorded at request time. Deployment history tells you what was live in a window, which breaks down during canaries when two versions serve simultaneously.
</details>

---

### Question 13
**Scenario:** A model update must be rolled back quickly if error rates rise.

A. Rebuild the old model from source and redeploy it, which restores the previous behavior once the build completes
B. Keep the previous version loaded and shift traffic back, with an automated trigger on the error-rate SLO
C. Restore the previous model from a nightly backup of the serving host and restart the server on that snapshot, then wait for it to warm up
D. Retrain

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rollback speed is set by whether the previous artifact is already loaded and routable. Rebuilding or restoring turns a 30-second recovery into hours. Automating the trigger removes the human latency during the window that matters most.
</details>

---

### Question 14
**Scenario:** Multiple teams share a GPU cluster and cost must be attributed.

A. Do not attribute costs
B. Estimate each team's share from its headcount and budget size, without looking at any GPU usage data at all
C. Split the bill evenly across teams every month, which is simple and avoids disputes about how GPU-hours were counted
D. Label workloads by team, collect GPU-hours per label from DCGM, and report showback or chargeback

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Attribution needs a label applied at submission time and metrics keyed by it, which is a policy decision as much as a technical one. Even splits remove any incentive to release idle capacity, which is where most GPU waste comes from.
</details>

---

### Question 15
**Scenario:** A post-incident review is scheduled after a serving outage.

A. Add more monitoring dashboards across the whole platform so that every future outage is visible to everyone at a glance
B. Close the ticket once service is restored and the dashboards have stayed green for a full day
C. Identify the engineer who caused it, so that the team can retrain them and prevent a repeat
D. Build the timeline, find the detection and mitigation gaps, and assign owned actions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Blameless review focuses on the conditions that let the failure happen and stay undetected. The output that matters is a small number of specific, owned actions, most often a missing alert, a missing guardrail, or a rollback path that was slower than assumed.
</details>

---

### Question 16
**Scenario:** A fraud model scores well offline but poorly in production. Investigation shows that the training pipeline and the online service compute the "days since last purchase" feature with different code.

A. Retrain the model more often so that it adapts to whatever values the online service produces
B. Add more training data from the offline pipeline so that the model generalizes to the online values
C. Define features once and serve the same definitions to training and inference, as a feature store does
D. Log the online feature values and ignore the gap, since small differences never affect model quality

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** This is training-serving skew: the model learned from one definition of a feature and is scored on another. A single shared definition, which a feature store provides for both offline and online paths, removes the mismatch at its source. Retraining or adding data does not fix inputs that are computed differently, and skew is a common cause of silent quality loss.

**Key Concept:** [Feast feature store documentation](https://docs.feast.dev/)
</details>

---

### Question 17
**Scenario:** A training run from three months ago cannot be reproduced, although the code and data are unchanged. The job had used the container tag `pytorch:latest`.

A. Reference containers by immutable digest or a dated release tag, and record it with each run's metadata
B. Rebuild the container from the current Dockerfile, since rebuilding gives the same image every time
C. Switch to a newer GPU, because reproducibility problems after three months usually come from hardware
D. Store only the model weights, since the environment never affects how a training run turns out

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A moving tag such as `latest` points to different images over time, so framework, CUDA and library versions changed silently. Pinning an immutable digest or a specific release (NGC containers use dated tags like `YY.MM`) and recording it makes the environment part of the lineage. Rebuilding pulls newer packages, hardware is not the likely cause, and the environment clearly matters.

**Key Concept:** [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
</details>

---

### Question 18
**Scenario:** A new recommendation model must be tested on real production traffic, but its responses must not reach users until it is proven.

A. Replace the live model for one hour at night and switch back if complaints arrive the next morning
B. Route 50% of users to the new model at once and compare click-through rates after one week
C. Test only on last year's logged requests, since live traffic cannot be used without user exposure
D. Shadow deploy it: mirror live requests to it, log its outputs, and keep serving the current model

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A shadow deployment sends a copy of production traffic to the candidate and records its outputs and latency without returning them, so it is evaluated on real inputs with no user impact. A night-time swap and a 50% split both expose users. Historical logs are useful but miss current traffic patterns, which shadowing captures.

**Key Concept:** [Triton model management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html)
</details>

---

### Question 19
**Scenario:** A Triton server hosts dozens of models, and the platform team needs to load and unload individual models on demand without restarting the server.

A. Restart Triton with a new model repository path each time a model needs to be added or removed
B. Use the default `none` model control mode, which polls the repository and loads changes automatically
C. Start Triton with `--model-control-mode=explicit` and load or unload models via the API
D. Deploy one Triton server per model so that adding a model never touches an existing server process

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In explicit mode, Triton loads only the models it is told to load, and the model repository API loads, reloads and unloads individual models while the server keeps serving the others. Restarting interrupts every model. The `none` mode loads everything at startup and does not react to changes (polling is a separate mode), and one server per model wastes GPUs.

**Key Concept:** [Triton model management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html)
</details>

---

### Question 20
**Scenario:** A Triton-served image model gets many small requests, and GPU throughput is low because each request runs as its own batch of one.

A. Enable dynamic batching in the model configuration, with a small maximum queue delay
B. Ask every client to collect 32 images before sending, so each call is a full batch
C. Run more Triton instances on more GPUs, so that each batch of one finishes sooner
D. Lower the model's precision to INT4, which batches the small requests automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Triton's dynamic batcher combines individual requests on the server into larger batches, and a short queue delay bounds the extra latency spent waiting for more requests. Client-side batching pushes complexity onto every caller and adds latency for slow callers. More GPUs spend more to process the same inefficient batches, and precision has nothing to do with batching.

**Key Concept:** [Triton batchers](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html)
</details>

---

### Question 21
**Scenario:** An LLM service handles very long prompts with short answers. Long prefill work keeps stalling token generation for other users on the same GPUs.

A. Shorten every prompt to a fixed size, so that prefill work is the same for every request
B. Turn off the KV cache, which removes the memory pressure caused by long prompt inputs
C. Use disaggregated serving, as in NVIDIA Dynamo, with separate prefill and decode workers
D. Raise the maximum batch size until both phases fit together on each GPU at the same time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Prefill is compute-bound and decode is memory-bandwidth-bound, so running them on the same GPUs lets long prefills interfere with steady token generation. Disaggregated serving places them in separate worker pools that scale independently, and Dynamo transfers the KV cache between them. Truncating prompts loses information, disabling the KV cache makes decoding far slower, and a bigger batch does not remove the interference.

**Key Concept:** [NVIDIA Dynamo documentation](https://docs.nvidia.com/dynamo/latest/index.html)
</details>

---

### Question 22
**Scenario:** `nvidia-smi` reports 100% GPU utilization for an inference service, yet the service is far below the GPU's expected throughput.

A. The GPU is fully used, because 100% utilization means every streaming multiprocessor is busy
B. Replace the GPU, because 100% utilization with low throughput always means a hardware fault
C. Lower the batch size until utilization falls below 100%, which shows the GPU has spare capacity
D. Check DCGM profiling metrics such as SM activity, since utilization only shows a kernel ran

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The basic GPU utilization figure is the share of time at least one kernel was running, so one small kernel can show 100% while most SMs sit idle. DCGM's profiling fields, such as SM active and tensor pipe active, show how much of the GPU is actually doing work. It is not proof of saturation, it does not indicate a fault, and shrinking batches lowers efficiency further.

**Key Concept:** [DCGM feature overview](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html)
</details>

---

### Question 23
**Scenario:** A Kubernetes GPU cluster needs GPU metrics in Prometheus, and the team also wants a few extra DCGM fields beyond the default set.

A. Deploy DCGM Exporter, often via the GPU Operator, with a custom metrics file of extra fields
B. Run `nvidia-smi` in a cron job on each node and push its text output to Prometheus through a gateway
C. Install the Prometheus node exporter, which collects every DCGM field from the GPUs automatically
D. Enable Kubernetes metrics-server, which reports GPU memory and SM activity for every pod by default

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DCGM Exporter exposes DCGM fields in Prometheus format, the GPU Operator can deploy it as a DaemonSet, and its metrics are configurable through a CSV of field IDs. Scraping `nvidia-smi` text is brittle and misses profiling fields. The node exporter collects host metrics, not DCGM data, and metrics-server reports CPU and memory for autoscaling.

**Key Concept:** [DCGM Exporter](https://docs.nvidia.com/datacenter/dcgm/latest/gpu-telemetry/dcgm-exporter.html)
</details>

---

### Question 24
**Scenario:** The operations team wants each node's GPUs checked continuously for problems such as memory, PCIe, NVLink and thermal faults, with alerts, rather than finding issues when jobs crash.

A. Run `dcgmi diag -r 4` every hour on every node, since the long diagnostic is the only health check DCGM offers
B. Watch the job logs for CUDA errors and open an investigation whenever a user reports a failed run
C. Enable DCGM health watches for the relevant subsystems and alert on warnings and failures they report
D. Reboot each node daily, since a reboot clears most GPU faults before they can affect running work

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DCGM health watches run in the background with little overhead and report the health of subsystems such as memory, PCIe, NVLink and thermals, so problems surface as alerts before or as they affect jobs. The long diagnostic is an intrusive stress test meant for maintenance windows, not hourly use. Waiting for user reports is reactive, and reboots hide faults instead of detecting them.

**Key Concept:** [DCGM feature overview](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html)
</details>

---

### Question 25
**Scenario:** Jobs keep landing on GPU nodes with latent faults, and users lose hours before anyone notices the bad node.

A. Ask users to report bad nodes in a shared spreadsheet, which the operations team checks every week
B. Run health checks before and between jobs, and cordon or drain any node that fails them automatically
C. Run every job on twice as many nodes as needed, so that losing a faulty node does not stop the work
D. Disable error reporting on the nodes, because Xid messages slow down the jobs that are running

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automated health checks, for example DCGM diagnostics or health watches in a prolog, epilog or node checker, remove a failing node from scheduling before it can take down more jobs. A weekly spreadsheet is far too slow. Doubling node counts doubles cost without removing the bad node, and suppressing error reporting hides the evidence.

**Key Concept:** [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html)
</details>

---

### Question 26
**Scenario:** A new driver and CUDA stack must be rolled out to a 400-node inference fleet, and the team wants to catch problems before they reach most of the fleet.

A. Upgrade all 400 nodes at once during a maintenance window to keep the fleet consistent
B. Let each node upgrade itself whenever a new package appears in the repository it uses
C. Upgrade only the nodes that report errors, leaving the healthy nodes on the old driver
D. Upgrade a small canary pool, check health and SLOs, then continue in wider waves

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A canary pool exposes the new stack to real traffic on a few nodes, and widening waves with health and SLO checks between them limits the blast radius of a bad release. An all-at-once upgrade risks the whole fleet. Uncontrolled self-upgrades create version drift, and upgrading only failing nodes leaves the fleet split by accident.

**Key Concept:** [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)
</details>

---

### Question 27
**Scenario:** An LLM inference deployment autoscales on CPU utilization, and it scales too late: latency rises long before CPU usage moves.

A. Scale on serving metrics that track load, such as queue time, requests in flight or KV cache usage
B. Lower the CPU threshold to 5% so that the deployment adds replicas as soon as any traffic arrives
C. Disable autoscaling and run the peak replica count all day, since inference load cannot be predicted
D. Scale on node disk usage, because model caches grow as traffic increases on each serving node

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** GPU inference load shows up in serving metrics, such as queue time, concurrency and KV cache utilization, well before CPU moves, so those are the right autoscaling signals. A tiny CPU threshold scales on noise. Running at peak all day wastes GPUs, and disk usage is not a load signal.

**Key Concept:** [Triton metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/metrics.html)
</details>

---

### Question 28
**Scenario:** An inference service has a 99.9% monthly availability SLO. The team wants pages only when reliability is genuinely at risk, not on every brief error spike.

A. Page on every single 5xx response, since any error at all means the SLO might be missed
B. Page only at the end of the month, when the SLO report shows whether the target was met
C. Alert on error budget burn rate, paging fast for a high burn and ticketing a slow burn
D. Alert when average CPU utilization exceeds 80%, which is a direct measure of the SLO

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Burn-rate alerting measures how quickly the error budget is being consumed, so a fast burn pages immediately while a slow burn creates a ticket, which ties alerts to user impact. Paging on every error causes alert fatigue. A month-end check is too late to act, and CPU utilization is not an availability measure.

**Key Concept:** [Alerting on SLOs (Google SRE Workbook)](https://sre.google/workbook/alerting-on-slos/)
</details>

---

### Question 29
**Scenario:** Minutes after a new model version is deployed, the error rate jumps and users are affected. The on-call engineer is not yet sure why.

A. Keep the new version live and debug in production, since rolling back loses the evidence of the fault
B. Roll back to the last known good version first, then investigate using the logs and metrics captured
C. Restart every GPU node in the serving fleet, since a restart fixes most errors after a deployment
D. Wait for the root cause to be confirmed before taking any action, so the change made is the right one

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Incident response puts mitigation first: when a change correlates with user impact, roll it back to restore service, and investigate afterwards from the telemetry already captured. Debugging live prolongs the outage. Restarting nodes is a guess that does not undo the change, and waiting for root cause leaves users affected.

**Key Concept:** [Triton model management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html)
</details>

---

### Question 30
**Scenario:** Throughput on one node drops every afternoon. DCGM shows the GPU clocks falling at those times, with clock event reasons pointing to thermal slowdown.

A. Raise the GPU power limit, which keeps the clocks high even when the GPU is too hot
B. Reinstall the driver, because clock reductions are caused by a corrupt driver install
C. Move the workload to fewer GPUs, so that each GPU runs at a higher clock speed
D. Check the node's cooling, airflow and inlet temperature, since the GPUs are throttling

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** DCGM reports why clocks were reduced, and a thermal reason with a time-of-day pattern points at cooling: blocked airflow, failed fans or a hot aisle when room load peaks. Raising the power limit makes the GPU hotter and does not override thermal protection. Driver corruption does not produce thermal events, and concentrating work raises temperatures further.

**Key Concept:** [DCGM feature overview](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html)
</details>

---

## Where to go deeper

- [NCP-AIO cert page](../nvidia/ai-operations-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the infrastructure counterpart
- [Observability basics](https://cloud.noblerworks.com/learn/concepts/observability-basics/) - the monitoring foundation
- [SRE and reliability topic index](https://cloud.noblerworks.com/topics/sre-and-reliability/) - SLOs and incident practice
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
