# Classical Baseline: Satellite Task Scheduling

## Overview

This notebook establishes a **classical optimization baseline** for the Satellite Task Scheduling problem.  
The objective is to compute **provably optimal schedules** under realistic operational constraints and use them as a **reference benchmark** for later **QAOA-based quantum scheduling experiments**.

Using a classical baseline is essential because:
- It provides a **ground-truth optimum**
- It allows **quantitative comparison** with quantum heuristics
- It helps validate constraint encoding and cost-function design before moving to quantum models

---

## Problem Objectives

The scheduling problem aims to **select the best subset of tasks** such that:
- The **energy budget** is not exceeded
- **Higher-priority tasks** are preferred
- Tasks are executed **only during valid visibility windows**

The optimization is performed **separately for each visibility window**, simplifying analysis and enabling modular quantum formulations later.

---

## Constraints (Detailed Explanation)

### 1. Energy Budget Constraint

The satellite has a **fixed energy capacity**:

- **Total Energy Budget = 5 units**

Each task consumes a known amount of energy.  
If the total energy of selected tasks exceeds this limit, the schedule is **physically infeasible** and therefore rejected.

**Why this constraint is critical:**
- Satellite subsystems (imaging, communication, experiments) draw from a shared power source
- Over-scheduling can cause mission failure or system shutdown
- Enforcing this constraint ensures **realistic scheduling**

Mathematically:

$$
\sum_{i \in S} E_i \leq 5
$$

Where:
- $S$ is the set of selected tasks
- $E_i$ is the energy cost of task $i$

Any violation results in an **invalid schedule**.

---

### 2. Task Priority Encoding

Each task has an associated **mission importance**, encoded numerically:

| Priority Level | Numerical Weight |
|----------------|------------------|
| High           | 3                |
| Medium         | 2                |
| Low            | 1                |

**Why numeric encoding is required:**
- Optimization algorithms require scalar objective values
- Priority weights allow **quantitative trade-offs** between tasks
- Enables smooth integration into classical and quantum cost functions

Higher values indicate **greater mission value**.

---

### 3. Visibility Window Constraint

Each task can only be executed during specific orbital visibility windows:

- **W1, W2, W3**

A task is **eligible for scheduling only within its assigned window**.

**Why windows are treated separately:**
- Satellite visibility changes due to orbital motion
- Tasks outside visibility are physically impossible
- Window-wise separation reduces complexity and mirrors real mission planning

Formally:

$$
S(W_k) \subseteq \{ \text{Tasks visible in window } W_k \}
$$

---

## Task Definition

Each task is described by:
- Energy cost
- Priority weight
- Visibility window

### Task Table

| Task | Description                  | Energy | Priority | Window |
|------|------------------------------|--------|----------|--------|
| T1   | High-res Earth Imaging        | 2      | High (3) | W1     |
| T2   | Ground Data Communication     | 1      | Medium (2) | W1 |
| T3   | Weather Sensing Operation     | 3      | High (3) | W2     |
| T4   | Scientific Experiment         | 3      | Low (1)  | W3     |

---

## Cost Function 

### Mathematical Form

The optimization objective balances **energy consumption** and **task priority**:

$$
\text{Cost} =\text{Total Energy}-\alpha \times \text{Total Priority}
$$

Where:
- **Total Energy** = sum of energies of selected tasks
- **Total Priority** = sum of priority weights of selected tasks
- $\alpha$ = tunable importance factor for mission priority

---

### Why This Cost Function Is Used

1. **Energy minimization**
   - Encourages efficient use of limited satellite power

2. **Priority maximization**
   - Rewards selection of mission-critical tasks

3. **Linear structure**
   - Easy to compute classically
   - Directly convertible into **QUBO / Ising Hamiltonians** for QAOA

4. **Trade-off control via $\alpha$**
   - Small $\alpha$: favors low energy usage
   - Large $\alpha$: favors high-priority missions

---

### Invalid Schedule Handling

Any schedule violating the energy constraint is assigned:

$$
\text{Cost} = \infty
$$

**Why this is necessary:**
- Prevents infeasible solutions from being chosen
- Simplifies optimization logic
- Matches penalty-based constraint enforcement in quantum algorithms

---

## Optimization Strategy (Classical Baseline)

For each visibility window:

1. Enumerate **all possible task subsets**
2. Compute total energy and priority
3. Reject subsets exceeding the energy budget
4. Evaluate the cost function
5. Select the subset with **minimum cost**

This exhaustive approach guarantees the **global optimum**, making it ideal as a benchmark.

---

## Visibility Window Analysis

---

## Visibility Window W1

### Available Tasks
- T1: Energy = 2, Priority = 3
- T2: Energy = 1, Priority = 2

### Candidate Schedules

| Tasks Selected | Total Energy | Total Priority | Cost |
|---------------|--------------|----------------|------|
| {T1}          | 2            | 3              | $2 - 3\alpha$ |
| {T2}          | 1            | 2              | $1 - 2\alpha$ |
| {T1, T2}      | 3            | 5              | $3 - 5\alpha$ |

### Optimal Schedule (W1)

- **Selected Tasks**: {T1, T2}
- **Energy Used**: 3
- **Total Priority**: 5

<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/e7acb5a1-4fc2-4bac-8723-376fb0db4155" />


---

## Visibility Window W2

### Available Tasks
- T3: Energy = 3, Priority = 3

### Optimal Schedule (W2)

- **Selected Tasks**: {T3}
- **Energy Used**: 3
- **Total Priority**: 3

<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/d723787f-a739-4060-a7e2-b7a99593e853" />


---

## Visibility Window W3

### Available Tasks
- T4: Energy = 3, Priority = 1

### Optimal Schedule (W3)

- **Selected Tasks**: {T4}
- **Energy Used**: 3
- **Total Priority**: 1

<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/dad3d423-cd22-4288-b12a-88f0d50e2df1" />


---

## Summary of Classical Optimal Schedules

| Window | Selected Tasks | Energy Used | Total Priority |
|--------|----------------|-------------|----------------|
| W1     | T1, T2         | 3           | 5              |
| W2     | T3             | 3           | 3              |
| W3     | T4             | 3           | 1              |

---

## Why This Baseline Matters for QAOA

This classical solution:
- Defines the **optimal reference energy**
- Enables **approximation ratio evaluation**
- Validates constraint penalties
- Ensures correctness before scaling to quantum hardware

---


---

