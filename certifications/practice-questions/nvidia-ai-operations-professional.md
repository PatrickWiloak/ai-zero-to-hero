---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - AI Operations (NCP-AIO) - Practice Questions

15 questions for NCP-AIO prep, evenly weighted across MLOps and model lifecycle, deployment and serving, GPU monitoring with DCGM, fleet management, and incident response (20% each).

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

## Where to go deeper

- [NCP-AIO cert page](../nvidia/ai-operations-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the infrastructure counterpart
- [Observability basics](https://cloud.noblerworks.com/learn/concepts/observability-basics/) - the monitoring foundation
- [SRE and reliability topic index](https://cloud.noblerworks.com/topics/sre-and-reliability/) - SLOs and incident practice
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
