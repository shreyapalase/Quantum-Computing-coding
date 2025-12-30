# Step 3: Binary Decision Variables and Objective Function  
### Connecting Satellite Scheduling to Quantum Optimization

---

## 1. Introduction

After defining a realistic satellite mission scenario and its constraints, the next step is to **translate the scheduling problem into decision variables and objectives** that can be optimized.

This step is crucial because:
- Optimization algorithms (classical or quantum) operate on **variables**
- QAOA specifically works with **binary decision variables**
- The way we define these variables determines how well the real problem is represented

In this step, we introduce **binary decision variables**, explain their real-world meaning, and define the **optimization objective** in clear, intuitive terms.

---

## 2. Why Decision Variables Are Needed

At its core, satellite task scheduling is a **decision-making problem**.

For each task, the satellite must decide:
- Should this task be executed?
- Or should it be skipped to save resources?

These yes/no decisions are naturally modeled using **binary variables**.

---

### Binary Decision Variable Definition

We define a binary decision variable for each task as:

$$
x_i =
\begin{cases}
1, & \text{if task } i \text{ is executed} \\
0, & \text{if task } i \text{ is skipped}
\end{cases}
$$

where:

- $i \in \{1, 2, 3, 4\}$ represents tasks **T1, T2, T3, and T4**
- Each variable $x_i$ captures a single scheduling decision (execute or skip)
- Each variable captures **one scheduling decision**

---

## 4. Decision Interpretation

Each binary variable directly corresponds to a real operational choice.

| Variable | Interpretation |
|--------|---------------|
| x₁ = 1 | Execute high-resolution Earth imaging (T1) |
| x₁ = 0 | Skip Earth imaging |
| x₂ = 1 | Perform ground communication (T2) |
| x₂ = 0 | Skip communication |
| x₃ = 1 | Execute weather sensing (T3) |
| x₃ = 0 | Skip weather sensing |
| x₄ = 1 | Perform scientific experiment (T4) |
| x₄ = 0 | Skip scientific experiment |

This formulation ensures:
- No ambiguity in decision-making
- Easy mapping from optimization output to real actions

---

## 5. Why Binary Variables Are a Natural Choice

### 5.1 Nature of Satellite Tasks

Most satellite tasks are:
- **Indivisible** (cannot be partially executed)
- **Discrete** (either completed or not)
- **Time-constrained**

Binary variables naturally reflect this reality.

---

### 5.2 Simplicity and Scalability

Binary variables:
- Reduce complex decisions to simple logic
- Scale well with the number of tasks
- Are widely used in scheduling and resource allocation problems

---

## 6. Why Binary Variables Fit Quantum Computing

Quantum optimization algorithms like **QAOA** are designed to work with:
- Binary variables
- Spin-like representations
- Quadratic objective functions

### Key Mapping
| Optimization Concept | Quantum Interpretation |
|---------------------|-----------------------|
| Binary variable (0/1) | Qubit state |
| 0 | |0⟩ state |
| 1 | |1⟩ state |
| Objective function | Cost Hamiltonian |
| Constraints | Penalty terms |

This makes binary scheduling problems **ideal candidates for quantum optimization**.

---

## 7. Objective of the Optimization Problem

The satellite scheduler has **multiple goals**, which often conflict with each other.

The objective is to:

> **Maximize mission value while minimizing resource usage and conflicts.**

We break this into **three components**.

---

## 8. Objective Component 1: Maximize Task Priority

Each task has a priority reflecting its importance.

### Intuition
- High-priority tasks should be favored
- Low-priority tasks should be selected only if resources allow

### Plain English Objective
> Prefer solutions where high-priority tasks are executed.

### Example
- Executing T1 and T3 (both high priority) is more valuable than executing T2 and T4.

---

## 9. Objective Component 2: Minimize Energy Usage

Energy is a limited and critical resource.

### Intuition
- High-energy tasks reduce future operational capability
- Efficient schedules extend satellite lifetime

### Plain English Objective
> Avoid selecting tasks that consume excessive energy unless they provide high value.

This introduces a **trade-off**:
- High priority vs high energy cost

---

## 10. Objective Component 3: Minimize Visibility Conflicts

Visibility windows restrict when tasks can be executed.

### Conflict Example
- T1 and T2 both require visibility window W1
- Satellite can execute only one task in W1

### Plain English Objective
> Penalize schedules that attempt to execute multiple tasks in the same visibility window.

This ensures:
- Physical feasibility
- Conflict-free scheduling

---

## 11. Combined Objective (Conceptual Form)

Putting everything together, the scheduler aims to:

> **Select a set of tasks that gives high total priority, uses low total energy, and avoids visibility window conflicts.**

This combined objective will later be expressed mathematically as:
- A weighted sum of priorities
- Energy penalties
- Conflict penalties

---

## 12. Example Interpretation Using Binary Variables

Consider the decision vector:

\[
(x_1, x_2, x_3, x_4) = (1, 0, 1, 0)
\]

This means:
- Execute T1 (Earth imaging)
- Skip T2 (communication)
- Execute T3 (weather sensing)
- Skip T4 (scientific experiment)

This choice:
- Selects both high-priority tasks
- Uses energy efficiently
- Avoids visibility conflicts

---

## 13. Why This Step Is Critical for QAOA

This binary formulation:
- Converts a real-world problem into a **combinatorial optimization problem**
- Allows direct construction of:
  - Objective function
  - Constraint penalties
  - QUBO matrix
- Enables mapping to:
  - Ising Hamiltonian
  - QAOA quantum circuits

Without this step, applying quantum algorithms would not be possible.

---

## 14. Summary

In this step, we:
- Defined binary decision variables for each task
- Explained their real-world meaning
- Justified why binary formulation is appropriate
- Defined optimization objectives in plain English
- Established the foundation for mathematical modeling

This step completes the **conceptual bridge** between satellite operations and quantum optimization.

---

## Author & Document Information

**Author:** Shreya Sunil Palase(CodeQubit)  

**Affilation:** Independent Researcher

**Project:** QAOA-Based Energy-Efficient Satellite Task Scheduling  

**Date:** 30 December 2025  

---
