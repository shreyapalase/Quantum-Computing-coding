# Step 5: Optimization Objective Function  
### Maximizing Mission Value Under Energy and Visibility Constraints

---

## 1. Introduction

After defining decision variables and constraints, the next step is to define **what the optimization is trying to achieve**.

In satellite task scheduling, the objective is not simply to execute as many tasks as possible. Instead, the scheduler must **balance mission value against limited resources and operational constraints**.

This step defines a **single optimization objective** that:
- Encourages valuable task execution
- Discourages infeasible or inefficient schedules
- Can be directly translated into a QUBO / QAOA formulation

---

## 2. What Is the Optimization Objective?

### Plain English Definition

> **The objective is to select a set of tasks that maximizes total mission value while respecting energy limits and avoiding visibility conflicts.**

This means:
- Prefer high-priority tasks
- Avoid wasting energy
- Ensure the schedule is physically feasible

---

## 3. Mission Value: What Are We Maximizing?

Mission value represents **how useful a schedule is** to the overall satellite mission.

It depends on:
- Task priority
- Scientific, commercial, or operational importance
- Time sensitivity of the task

Higher mission value means:
- More critical data collected
- Better mission performance
- Higher return on mission cost

---

## 4. Decomposing the Objective Function

To model this formally, the objective function is divided into **two complementary parts**:

1. **Reward Term** – encourages desirable behavior  
2. **Penalty Term** – discourages constraint violations  

This structure is standard in constrained optimization and especially important for QUBO and QAOA.

---

## 5. Reward Term: Maximizing Task Priority

### 5.1 Conceptual Meaning

The reward term captures the **positive benefit** of executing tasks.

Each task is assigned a numerical priority value:
- High priority → large reward
- Medium priority → moderate reward
- Low priority → small reward

---

### 5.2 Plain English Description

> If a task is executed, the mission gains value equal to its priority.

Skipping a task yields no reward.

---

### 5.3 Conceptual Mathematical Form

Let:
- $p_i$ be the priority value of task $i$
- $x_i \in \{0,1\}$ be the binary decision variable

The reward term is:

$$
\text{Reward} = \sum_{i=1}^{N} p_i x_i
$$

---

### 5.4 Interpretation

- Selecting a high-priority task increases the objective significantly
- Selecting low-priority tasks contributes less
- The optimizer naturally prefers valuable tasks

This term alone would cause the optimizer to select **all tasks**, which is why penalties are required.

---

## 6. Penalty Term: Enforcing Constraints

The penalty term reduces the objective value when constraints are violated.

Instead of explicitly forbidding infeasible solutions, penalties:
- Make infeasible solutions unattractive
- Allow all decisions to be expressed in a single objective function

---

### 6.1 Energy Penalty

#### Plain English Meaning

> If the total energy used exceeds the available energy budget, the schedule is penalized.

This discourages selecting too many energy-intensive tasks.

---

#### Conceptual Form

Let:
- $e_i$ be the energy cost of task $i$
- $E_{\max}$ be the maximum available energy

The energy penalty increases when:

$$
\sum_{i=1}^{N} e_i x_i > E_{\max}
$$

---

### 6.2 Visibility Conflict Penalty

#### Plain English Meaning

> If two tasks that require the same visibility window are selected, the schedule is penalized.

This ensures that conflicting tasks are not executed simultaneously.

---

#### Conceptual Form

For any conflicting task pair $(i, j)$:

$$
\text{Penalty}_{\text{vis}} \propto x_i x_j
$$

This quadratic structure is **especially important** for QUBO and QAOA.

---

## 7. Combined Objective Function (Conceptual)

Putting everything together, the optimization objective becomes:

> **Maximize total reward from task execution while minimizing penalties due to energy overuse and visibility conflicts.**

Conceptually:

$$
\text{Objective} =\text{Reward}-\text{Penalty}_{\text{energy}}-\text{Penalty}_{\text{visibility}}
$$

Weights can be applied to penalties to ensure:
- Constraint satisfaction is prioritized over reward maximization

---

## 8. What Does an Optimal Solution Mean?

An **optimal solution** is not simply the one with the highest reward.

### An optimal schedule:
- Satisfies all hard constraints
- Maximizes total mission value
- Uses energy efficiently
- Avoids visibility conflicts

---

### Example Interpretation

If the optimizer selects:
- Fewer tasks
- But all are high priority
- And no constraints are violated

Then this solution is **better** than a schedule that selects many low-value or infeasible tasks.

---

## 9. Trade-Offs Captured by the Objective

The objective function captures key real-world trade-offs:

- High priority vs high energy cost  
- Task quantity vs feasibility  
- Immediate reward vs long-term mission health  

These trade-offs define the **shape of the optimization landscape**.

---

## 10. Why This Objective Is Suitable for QAOA

This objective:
- Is expressed using binary variables
- Can be written as a quadratic function
- Naturally maps to QUBO
- Translates directly into an Ising Hamiltonian

This makes it ideal for:
- QAOA
- Hybrid quantum–classical solvers

---

## 11. Summary

In this step, we:
- Defined the optimization objective clearly
- Explained mission value in intuitive terms
- Separated reward and penalty components
- Explained what optimality means in practice
- Prepared the model for QUBO and QAOA formulation

This step completes the **optimization problem definition**.

---

## Author & Document Information

**Author:** Shreya Sunil Palase (codeQubit)

**Affiliation:** Independent-Reasearcher

**Project:** QAOA-Based Energy-Efficient Satellite Task Scheduling

**Date:** 30 December 2025  

---
