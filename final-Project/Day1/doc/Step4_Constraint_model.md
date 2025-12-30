# Step 4: Constraint Identification and Explanation  
### Defining Feasible Satellite Schedules for Optimization

---

## 1. Introduction

In optimization problems, the **objective function defines what we want**, while **constraints define what is allowed**.

For satellite task scheduling, constraints arise directly from:
- Physical limitations of space systems
- Orbital mechanics
- Mission-level operational rules

A schedule that violates any constraint is **physically infeasible**, regardless of how high its objective value may be.  
Therefore, correctly identifying and modeling constraints is essential before applying **QAOA or any optimization algorithm**.

---

## 2. Overview of Key Constraints

In this work, we focus on three fundamental constraints:

1. **Energy Budget Constraint**  
2. **Visibility Window (Conflict) Constraint**  
3. **Mandatory High-Priority Task Constraint**

These constraints capture the most critical real-world limitations faced by a satellite.

---

## 3. Constraint 1: Energy Budget Constraint

### 3.1 Real-World Motivation

Satellites operate on a **limited energy supply** provided by solar panels and onboard batteries.  
Energy is consumed by:
- Payload instruments
- Communication systems
- Attitude control mechanisms
- Onboard computation

Once the battery is depleted:
- Tasks cannot be executed
- Satellite health may be compromised
- Mission lifetime is reduced

---

### 3.2 Constraint Description (Plain English)

> The total energy consumed by all selected tasks must not exceed the maximum available energy of the satellite.

This constraint ensures that the satellite **never schedules more work than it can physically support**.

---

### 3.3 Conceptual Mathematical Form

Let:
- $e_i$ be the energy cost of task $i$
- $E_{\max}$ be the available energy budget

Then the constraint is:

$$
\sum_{i=1}^{N} e_i x_i \leq E_{\max}
$$

---

### 3.4 Interpretation

- Each selected task ($x_i = 1$) contributes to energy consumption
- Skipped tasks ($x_i = 0$) contribute nothing
- The constraint enforces **global energy feasibility**

---

### 3.5 Why This Constraint Is Critical

- Prevents battery depletion
- Encourages energy-efficient scheduling
- Introduces trade-offs between high-value and high-cost tasks

In QAOA, this constraint will later be encoded as a **penalty term** in the cost Hamiltonian.

---

## 4. Constraint 2: Visibility Window Conflict Constraint

### 4.1 Real-World Motivation

Due to orbital motion, a satellite can only:
- Observe a target
- Communicate with a ground station
during **specific time windows**

Additionally:
- Satellites usually execute **only one task at a time**
- Overlapping visibility windows create task conflicts

---

### 4.2 Constraint Description (Plain English)

> If two tasks require the same visibility window and overlap in time, they cannot both be executed.

This reflects the physical impossibility of executing multiple conflicting tasks simultaneously.

---

### 4.3 Example from the Mission Setup

- Task T1 and Task T2 both require **Visibility Window W1**
- Executing both would require the satellite to perform two actions at the same time
- Therefore, only one of them can be selected

---

### 4.4 Conceptual Mathematical Form

For any pair of tasks $(i, j)$ that conflict:

$$
x_i + x_j \leq 1
$$

---

### 4.5 Interpretation

- If $x_i = 1$, then $x_j$ must be $0$
- This constraint enforces **mutual exclusivity**
- It significantly increases combinatorial complexity

---

### 4.6 Why This Constraint Is Important

- Ensures temporal feasibility
- Prevents physically impossible schedules
- Models real orbital and operational conflicts

In QAOA, these constraints naturally become **quadratic penalty terms**, making them well-suited for QUBO formulations.

---

## 5. Constraint 3: Mandatory High-Priority Task Constraint

### 5.1 Real-World Motivation

Certain tasks are **mission-critical**:
- Disaster response imaging
- Emergency communication
- Safety-related operations

Failure to execute these tasks may:
- Cause mission failure
- Lead to loss of critical data
- Have real-world consequences

---

### 5.2 Constraint Description (Plain English)

> All tasks classified as *high priority* must be scheduled, provided they are feasible within resource constraints.

This reflects **mission-level rules** rather than physical limitations.

---

### 5.3 Conceptual Mathematical Form

Let $\mathcal{H}$ be the set of high-priority tasks.

For each $i \in \mathcal{H}$:

$$
x_i = 1
$$

---

### 5.4 Interpretation

- High-priority tasks are **non-negotiable**
- Optimization is performed around them, not instead of them
- Lower-priority tasks must adapt

---

### 5.5 Practical Considerations

If a high-priority task:
- Violates energy constraints
- Conflicts with another mandatory task

Then:
- Mission planning must be revised
- Or additional resources must be allocated

This constraint highlights the importance of **feasibility analysis before optimization**.

---

## 6. Interaction Between Constraints

Constraints do not act independently.

### Example Interaction
- A high-priority task may consume large energy
- Executing it may force skipping multiple low-priority tasks
- Visibility conflicts may further restrict options

This interaction creates a **complex feasible region**, which motivates the use of advanced optimization techniques.

---

## 7. Why Constraint Modeling Matters for QAOA

QAOA requires:
- Clear binary variables
- Well-defined constraints
- Penalty-based formulations

Each constraint:
- Translates into a penalty term
- Shapes the cost landscape
- Influences quantum state evolution

Incorrect or incomplete constraints lead to:
- Invalid schedules
- Misleading optimization results

---

## 8. Summary

In this step, we identified and deeply explained three essential constraints:

1. **Energy Budget Constraint** — ensures power feasibility  
2. **Visibility Window Constraint** — enforces temporal exclusivity  
3. **Mandatory Task Constraint** — enforces mission priorities  

These constraints transform the scheduling problem from a simple selection task into a **structured, constrained optimization problem**.

---

## Author & Document Information

**Author:** Shreya Sunil Palase  

**Affilation**:Independent researcher

**Project:** QAOA-Based Energy-Efficient Satellite Task Scheduling  

**Date:** 30 December 2025  


---
