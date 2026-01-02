# QAOA Based Energy-Efficient Satellite Task Scheduling Under Orbital Visibility Constraints

---

## 1. Introduction

Satellite missions operate under severe resource limitations, particularly **restricted onboard energy** and **time-dependent orbital visibility**. Each operational task—such as imaging, communication, or sensing—must be carefully scheduled to maximize mission value while respecting these constraints.

This project presents a **conceptual and step-by-step formulation** of an **energy-efficient satellite task scheduling problem** solved using the **Quantum Approximate Optimization Algorithm (QAOA)**.  
Importantly, this document **does not focus on quantum circuit execution or calculations**, but instead explains **how each modeling step is performed** and **why it is required**, making the approach understandable from a systems and optimization perspective.

---

## 2. Classical Satellite Scheduling Problem (Brief Overview)

Classically, satellite task scheduling is a **binary decision problem**:

- Decide which tasks should be executed
- Maximize overall mission priority
- Respect:
  - Energy budget
  - Orbital visibility windows
  - Task conflicts

The challenge lies in balancing **high-priority tasks** against **limited energy and timing constraints**, which becomes computationally expensive as task count grows.

---

## 3. Step 1 – Problem Definition

### 3.1 Task Table

| Task | Energy Cost $$E_i$$ | Priority Weight $$P_i$$ | Visibility Window |
|----|----|----|----|
| T1 | 2 | 3 (High) | W1 |
| T2 | 1 | 2 (Medium) | W1 |
| T3 | 3 | 3 (High) | W2 |
| T4 | 2 | 1 (Medium) | W3 |

**Total Available Energy:**

$$
E_{\max} = 5
$$

### 3.2 Scheduling Decision

Each task is represented as a **binary decision**:

- Task selected → 1  
- Task not selected → 0  

The goal is to find the **best combination of selected tasks**.

---

## 4. Step 2 – Cost Hamiltonian (Objective Modeling)

### Purpose  
This step defines **what we want to optimize**.

### How It Is Performed  
- Higher-priority tasks are assigned higher weights.
- Selecting a task contributes positively to the total score.
- The model favors schedules that include tasks with higher mission importance.

### Conceptual Meaning  
> “Among all valid schedules, prefer those that maximize total mission priority.”

---

## 5. Step 3 – Cost Hamiltonian Layer

### Purpose  
This layer ensures that **priority information influences the optimization process**.

### How It Is Performed  
- The priority-based objective is applied uniformly across all possible task combinations.
- Schedules with higher total priority are favored during optimization.

### Conceptual Meaning  
> “Guide the search process toward schedules that are more valuable for the mission.”

---

## 6. Step 4 – Visibility Constraint Layer

### Purpose  
Tasks can only be executed during specific **orbital visibility windows**.

### How It Is Performed  
- Tasks assigned to incompatible visibility windows are discouraged from being selected together.
- Tasks sharing the same window are allowed if energy permits.

### Conceptual Meaning  
> “Do not allow schedules that violate orbital access constraints.”

---

## 7. Step 5 – Penalty Layer for Invalid Schedules

### Purpose  
To ensure that **constraint violations are not ignored**.

### How It Is Performed  
- Any schedule that violates visibility or structural constraints is penalized.
- The penalty increases the “cost” of invalid solutions.

### Conceptual Meaning  
> “Invalid schedules should always be worse than valid ones.”

---

## 8. Step 6 – Energy Penalty Layer

### Purpose  
Satellites have a **strict energy budget** that cannot be exceeded.

### How It Is Performed  
- The total energy of selected tasks is compared against the maximum available energy.
- If the energy budget is exceeded, a penalty is applied.

### Conceptual Meaning  
> “Even high-priority tasks are rejected if they consume too much energy.”

---

## 9. Step 7 – Mixer Layer

### Purpose  
To allow exploration of **different task combinations**.

### How It Is Performed  
- The model is allowed to move between alternative schedules.
- This prevents the optimization from getting stuck in a single poor solution.

### Conceptual Meaning  
> “Explore multiple scheduling possibilities instead of committing too early.”

---

## 10. Step 8 – Full QAOA-Based Scheduling Model

### How All Steps Work Together

- The **cost model** pushes toward high-priority tasks.
- The **visibility layer** enforces orbital feasibility.
- The **energy penalty layer** enforces power limitations.
- The **mixer layer** ensures exploration of alternatives.

Together, these steps create a balanced decision framework that naturally prefers **feasible, energy-efficient schedules**.

### we get ourfinal Quantum circuit as :
<img width="853" height="367" alt="image" src="https://github.com/user-attachments/assets/19d675ac-62f9-49ae-81fb-a411a4406187" />

---

## 11. Final Project Interpretation

After applying all steps of the QAOA-based modeling framework, the final outcome shows a **high selection probability for Task T4**.

### Why Task T4 Is Selected

- Fits comfortably within the energy budget
- Has a unique visibility window (W3), avoiding conflicts
- Introduces minimal penalties compared to other task combinations

### Key Insight

> Even though T4 does not have the highest priority, it represents the **most feasible and reliable scheduling choice** when all constraints are considered simultaneously.

This highlights a core strength of QAOA-style modeling:  
**feasibility and efficiency can outweigh raw priority.**

---

## 12. Placeholder for Experimental Results

### 12.1 Task Selection Probability Graph
<img width="855" height="393" alt="image" src="https://github.com/user-attachments/assets/72497ff5-55e6-4fc0-82c9-8331b340b269" />


---

### 12.2 Energy Utilization and Priority (like classical type)
<img width="547" height="433" alt="image" src="https://github.com/user-attachments/assets/ade23af4-d76e-40eb-8854-1a571e86f7de" />


---

## Why QAOA Selects **T4** Over Higher-Priority Tasks (T1 and T3)

## 1. Priority Is Not the Only Optimization Criterion

In this model, **priority is treated as a reward, not an absolute rule**.

The objective is:

> **Maximize mission value while strictly respecting energy and visibility constraints**

This means:
- A high-priority task is preferred **only if it is feasible**
- If a high-priority task causes constraint violations, its effective value is reduced

Thus, QAOA does **constraint-aware optimization**, not greedy priority selection.

---

## 2. Why T1 Is Penalized Despite High Priority

### Visibility Conflict
- T1 shares **Visibility Window W1** with T2
- Selecting T1 significantly reduces feasible combinations
- This introduces repeated penalty accumulation

### Optimization Impact
- Even though T1 has high priority, the **conflict risk lowers its net contribution**
- Many schedules containing T1 are invalid or near-penalty boundaries

---

## 3. Why T3 Is Penalized Despite High Priority

### Energy Dominance
- T3 consumes **3 out of 5 energy units**
- This leaves very little margin for other tasks

### Optimization Impact
- Any combination including T3 is fragile
- Small additions cause energy violations
- This heavily restricts feasible scheduling space

---

## 4. Why T4 Becomes Dominant

### Unique Visibility Window
- T4 operates in **W3**, which is exclusive
- No temporal or orbital conflicts

### Energy Efficiency
- Energy cost is moderate (2 units)
- Allows combination flexibility

### Feasibility Density
- T4 appears in **the largest number of valid schedules**
- The algorithm naturally assigns higher probability to such solutions

---

## 5. Key Optimization Insight 

> **QAOA maximizes feasible reward, not theoretical priority.**

High-priority tasks (T1, T3):
- Provide high reward
- But only in **narrow, high-risk regions**

T4:
- Provides lower reward
- But across **many valid configurations**

**Result:**  
T4 dominates the probability distribution.

---

## 6. Comparison Table: T4 vs T1 and T3 (Execution Perspective)

| Aspect | T1 | T3 | **T4** |
|-----|----|----|----|
| Priority Weight | High | High | Medium |
| Energy Usage | Moderate | **High** | Moderate |
| Visibility Window | Shared (W1) | Single (W2) | **Exclusive (W3)** |
| Conflict Probability | High | Medium | **None** |
| Energy Violation Risk | Medium | **High** | **Low** |
| Valid Schedule Count | Limited | Very Limited | **High** |
| Effective Optimization Weight | Reduced | Heavily Reduced | **Maximized** |
| Final Probability | Medium | Low | **Highest** |

---

Although T1 and T3 have higher individual priority, they introduce visibility and energy constraints that significantly reduce feasible scheduling combinations. T4 remains feasible across the largest number of valid schedules, so QAOA correctly assigns it the highest probability.”

---

## 7. Algorithm Specifications 

### Problem Characteristics
- **Problem Type:**  
  Constrained combinatorial optimization

- **Formal Class:**  
  NP-hard (binary quadratic optimization)

- **Decision Variables:**  
  Binary task-selection variables

---

### Algorithm Properties (QAOA-Based Model)

| Specification | Description |
|-------------|------------|
| Optimization Style | Constraint-aware maximization |
| Solution Nature | Probabilistic (distribution over schedules) |
| Constraint Handling | Penalty-based encoding |
| Scalability | Polynomial per iteration, exponential state space |
| Determinism | Non-deterministic |
| Output | Best feasible task set by probability |
| Hardware Suitability | NISQ-era quantum devices |
| Classical Equivalent | Quadratic Unconstrained Binary Optimization (QUBO) |

---

### Time & Space Complexity (Conceptual)

- **State Space:**  
  $$O(2^n)$$ possible schedules

- **Per-Iteration Cost:**  
  Polynomial in number of tasks

- **Overall Complexity:**  
  Exponential in theory, heuristic in practice

> Note: The algorithm is not used to enumerate all solutions but to bias the search toward optimal feasible regions.

---

## 13. Conclusion

This project demonstrates a **step-by-step conceptual application of QAOA** to satellite task scheduling without delving into quantum execution details. Each modeling layer serves a clear purpose, collectively ensuring that the final schedule is:

- Energy-efficient  
- Visibility-compliant  
- Operationally realistic  

The final dominance of Task T4 confirms that **constraint-aware optimization** is essential for real-world satellite operations.

---
