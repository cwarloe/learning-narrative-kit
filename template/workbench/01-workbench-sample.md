# Workbench 01 — Circuit Breakers & Backpressure Dynamics

## At a glance

- **Part of:** Dual-Track System Architecture & Resilience Curriculum
- **Follows:** [Chapter 01 (Story) — When the Queue Stood Still](#/narrative/01-chapter-sample)
- **Version:** 1.0 — Operational Specimen
- **Capability targets:** ARCH-1 (Queue Capacity Modeling), ARCH-2 (Backpressure Implementation), IR-2 (Failure Domain Isolation), TH-1 ([[falsifiable_hypothesis|Falsifiable Hypothesis Formulation]])
- **Time:** ~90 minutes
- **Workbench:** Python 3, CLI terminal, or simulated telemetry playground
- **Assumes:** Basic understanding of HTTP status codes, queue buffers, and JSON payloads.

---

## 1. Technical Heuristics & Mathematical Foundations

When managing ingestion queues under bursty workloads, queue depth is governed by **Little’s Law**:

$$L = \lambda \cdot W$$

Where:
- $L$ is the average number of events waiting in the queue buffer.
- $\lambda$ is the arrival rate of incoming telemetry events (events/second).
- $W$ is the average wait and processing time per event (seconds).

### The Saturation Collapse Threshold
If arrival rate $\lambda$ exceeds maximum consumer processing rate $\mu$, the buffer growth rate $R_{growth}$ expands linearly:

$$R_{growth} = \lambda - \mu \quad (\text{for } \lambda > \mu)$$

Without active [[backpressure|backpressure]], the time until out-of-memory kernel panic ($T_{oom}$) is strictly bounded by available memory $M_{avail}$ and average payload size $S_{avg}$:

$$T_{oom} = \frac{M_{avail}}{(\lambda - \mu) \cdot S_{avg}}$$

### Operational Rules of Thumb
1. **Never solve queue contention with heap expansion alone.** Expanding memory simply increases recovery time (GC pauses and replay lag) when the buffer inevitably fills.
2. **Backpressure must propagate to the edge.** If the edge gateway does not return HTTP 429 or pause socket reads, the queue is merely moving the failure point to another subsystem.
3. **Breakers must trip on latency, not just error rate.** Slow dependencies consume sockets longer than hard errors, exhausting connection pools.

---

## 2. Interactive Micro-Drills

### Drill W1.1: Spotting the Saturation Trigger

Review the three telemetry scenarios below. Which **one** indicates that a [[circuit_breaker|circuit breaker]] must trip to preserve cluster availability?

1. **Scenario A:** Ingestion latency jumps from 150 ms to 320 ms during peak morning load, but worker CPU utilization remains steady at 45% and memory buffer stays at 20%.
2. **Scenario B:** Consumer processing latency spikes to 4,800 ms on a single shard, buffer memory reaches 92%, and incoming [[cardinality|cardinality]] indicates one client account is generating 85% of incoming volume.
3. **Scenario C:** Downstream indexer returns HTTP 503 for a scheduled 10-second rolling restart while upstream gateways buffer messages in local disk queues.

<details class="reveal-gate">
  <summary>🔍 Check Evaluation Key</summary>
  <div class="reveal-content">
    <p><strong>Answer: Scenario B.</strong></p>
    <ul>
      <li><strong>Scenario A</strong> is normal organic peak traffic drift within acceptable operational parameters.</li>
      <li><strong>Scenario B</strong> represents an imminent catastrophic failure: localized buffer exhaustion driven by an anomalous high-cardinality tenant. Tripping the breaker on that tenant isolates the blast radius and enforces [[graceful_degradation|graceful degradation]].</li>
      <li><strong>Scenario C</strong> is a planned transient maintenance window safely absorbed by disk-backed queues.</li>
    </ul>
  </div>
</details>

---

## 3. Practice Application: Commit Before You Inspect

In this exercise, you evaluate an operational incident before inspecting the root-cause metrics.

### The Situation
You are monitoring an ingestion gateway receiving 25,000 requests/sec. At 14:02 UTC, downstream database response times increase from 12 ms to 1,200 ms. 

Your teammate proposes immediately increasing worker timeout limits from 2.0 seconds to 10.0 seconds so requests "have enough time to finish."

### Your Required Prediction Commitments
Before looking at the simulated system logs below, write down your answers to these five structural questions:

1. **Current Explanation:** What will happen to the number of concurrent open sockets if timeout is increased from 2s to 10s while arrival rate remains constant?
2. **Evidence Basis:** Which mathematical relationship (e.g. Little’s Law) justifies your expectation?
3. **Material Assumption:** What are you assuming about database throughput capacity under increased connection loads?
4. **Observable Prediction:** Formulate a [[falsifiable_hypothesis|falsifiable hypothesis]] naming a direction, an exact metric, and a falsification condition.
5. **What Would Weaken Your Model:** What observation would prove your hypothesis wrong?

<div class="prediction-gate">
  <h4>🔒 Stage 1: Commit Before You Reveal</h4>
  <p><strong>Strict Rule:</strong> Commit your 5 answers to your notes or scratchpad before opening the reveal gate below.</p>

  <details class="reveal-gate">
    <summary>🔓 I Have Written All 5 Commitments — Reveal System Telemetry</summary>
    <div class="reveal-content">
      <h5>Telemetry Output from Synthetic Benchmark Test</h5>
      
```console
$ lnk-benchmark-runner --load 25000rps --timeout 10s
[TEST] Applying 10.0s timeout to database client connection pool...
[TIME: 00:04] Concurrent open connections: 18,400 (Limit: 20,000)
[TIME: 00:06] Concurrent open connections: 20,000 [POOL EXHAUSTED]
[FATAL] Gateway error: socket: too many open files / connection refused
[FATAL] System state: 100% of incoming requests dropped across ALL tenants
```

      <h5>Expert Technical Debrief</h5>
      <p>Increasing timeouts under downstream saturation causes <strong>concurrency pileup</strong>: by Little's Law, if processing time $W$ increases by $5\times$ while arrival rate $\lambda$ stays constant, the number of in-flight connections $L$ must increase $5\times$. The connection pool exhausts in seconds, taking down the entire service.</p>
      <p>The correct architectural move is the inverse: <strong>shorten timeouts, trip the circuit breaker early, and shed non-essential load</strong> via [[backpressure|backpressure]].</p>
    </div>
  </details>
</div>

---

## 4. Hands-On Implementation: Fast Circuit Breaker in Python

Deploy this lightweight resilient circuit breaker pattern into your pipeline adapter:

```python
import time

class ResilientCircuitBreaker:
    """
    Zero-dependency Circuit Breaker implementation for high-throughput pipelines.
    States: CLOSED (normal), OPEN (tripped/failing fast), HALF_OPEN (probing recovery).
    """
    def __init__(self, failure_threshold: int = 3, recovery_time_sec: float = 10.0):
        self.failure_threshold = failure_threshold
        self.recovery_time_sec = recovery_time_sec
        self.failure_count = 0
        self.state = "CLOSED"
        self.last_failure_time = 0.0

    def can_execute(self) -> bool:
        if self.state == "CLOSED":
            return True
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_time_sec:
                self.state = "HALF_OPEN"
                return True
            return False
        return True  # HALF_OPEN allows single canary probe

    def record_success(self):
        self.failure_count = 0
        self.state = "CLOSED"

    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
```

---

## 5. Performance Deliverable: 1-Page Operational Resilience Brief

To complete this workbench, author a 1-page **Operational Resilience Specification** covering:

1. **Target Subsystem & Shard Topology:** Identify your high-risk queue boundaries.
2. **Cardinality Alert Rules:** Thresholds for distinct tenant or payload keys that trigger inspection.
3. **Backpressure Signaling Contract:** Explicit HTTP status codes (e.g. 429 vs 503) and client retry headers (`Retry-After`).
4. **Circuit Breaker Calibration:** Specific latency trip limits ($p99 > 1,500\text{ ms}$ for 3 checks) and canary recovery timeout.
5. **Verification Test:** Describe a [[synthetic_benchmark|synthetic benchmark]] scenario proving that single-tenant saturation cannot cascade to other workloads.

---

## 6. The 4DX Execution Scorecard

```
WEEKLY 4DX RESILIENCE SCORECARD — ENGINEER: [ _____________ ]  WEEK: [ ________ ]

[ WIG / LAG TARGET ]: Zero uncontained cascade failures; 100% adherence to backpressure standards.

[ LEAD MEASURE ]: % of queue modifications backed by a documented "Commit Before You Inspect" 
                  Prediction Sheet before running load tests. (Target: 100%)

  EXERCISE ID     PREDICTION COMMITTED?   BREAKER CALIBRATED?   DELIVERABLE VERIFIED?
  WORKBENCH-01            [   ]                  [   ]                  [   ]
  WORKBENCH-02            [   ]                  [   ]                  [   ]
  WORKBENCH-03            [   ]                  [   ]                  [   ]

  EXECUTION DISCIPLINE RATE: [ _____ / _____ ] = [ _____ % ]
```

---

<div class="bridge-card">
  <div class="bridge-label">Next Unit in Track</div>
  <div class="bridge-title">Chapter 02 — The Long Tail of Telemetry</div>
  <p class="bridge-desc">Advance to Chapter 02 to discover how Elena and Marcus apply least-frequency analysis to uncover stealthy configuration drift buried beneath millions of routine transactions.</p>
  <a href="#/narrative/01-chapter-sample" class="bridge-btn">Return to Chapter 01 Narrative →</a>
</div>
