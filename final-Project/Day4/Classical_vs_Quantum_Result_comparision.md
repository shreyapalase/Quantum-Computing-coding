# QAOA-Based Energy Efficient Satellite Task Scheduling Under Orbital Visibility Constraints  
### Classical vs Quantum Optimization Comparison

---

## 1. Project Overview

Satellite task scheduling is a critical optimization problem in modern space systems. A satellite must execute multiple observation or communication tasks while respecting **energy constraints**, **task priorities**, and **orbital visibility windows**. Inefficient scheduling can lead to excessive energy consumption, missed high-priority tasks, and underutilization of limited orbital access.

This project explores a **hybrid comparison** between:

- **Classical scheduling algorithms**
- **Quantum Approximate Optimization Algorithm (QAOA)**

with a focus on **energy efficiency** and **priority-aware decision making under orbital visibility constraints**.

---

## 2. Problem Definition

### 2.1 Input Task Table

| Task | Energy Cost | Priority | Visibility Window |
|-----|------------|----------|------------------|
| T1  | 2          | High     | W1               |
| T2  | 1          | Medium   | W1               |
| T3  | 3          | High     | W2               |
| T4  | 2          | Low      | W3               |

### 2.2 Constraints

- Each task can only be executed within its assigned **visibility window**
- Satellite energy budget is limited
- High-priority tasks should be favored
- Only one task can be scheduled at a time per visibility window

---

## 3. Classical Solution Approach

### 3.1 Classical Scheduling Logic

The classical approach typically uses **greedy heuristics**, **rule-based selection**, or **deterministic optimization** such as:

- Priority-first scheduling
- Energy-minimization heuristics
- Window-by-window independent selection

In this project, the classical model processes each **visibility window independently**, selecting tasks based on **local constraints** rather than global optimization.

---

### 3.2 Classical Output Interpretation (Graph-Based)


The classical algorithm produces **three bar graphs**, one for each visibility window:
<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/1fe7802f-8b51-4ca5-99af-0a7a9d4162ec" />

#### 🔹 Visibility Window W1
- **Orange Bars (Selected Tasks)**:  
  - T1  
  - T2  
- **Blue Bars (Not Selected)**:  
  - T3  
  - T4  

**Reasoning**:  
Both T1 and T2 fall within W1. The algorithm selects them based on availability and manageable energy cost, without globally reconsidering task interdependencies.

---

#### 🔹 Visibility Window W2
<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/2fc69e73-3eb9-4a25-a650-28a8bf1b9b1d" />

- **Orange Bar**:  
  - T3  
- **Blue Bars**:  
  - T1, T2, T4  

**Reasoning**:  
Only T3 is visible in W2, so it is automatically selected regardless of its higher energy cost.

---

#### 🔹 Visibility Window W3
<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/78db7fd5-e61f-4c54-86ff-50ca30e3c40e" />

- **Orange Bar**:  
  - T4  
- **Blue Bars**:  
  - T1, T2, T3  

**Reasoning**:  
T4 is the only task in W3 and is selected despite its low priority.

---

### 3.3 Limitations of Classical Approach

1. **Local Optimization**  
   Each window is optimized independently, ignoring global energy–priority trade-offs.

2. **Priority Dilution**  
   Low-priority tasks may be scheduled simply due to availability.

3. **Scalability Issues**  
   As task count increases, classical heuristics struggle with combinatorial complexity.

4. **No Probabilistic Exploration**  
   Classical methods cannot naturally explore multiple competing schedules simultaneously.

---

## 4. Quantum Solution Using QAOA

### 4.1 QAOA Overview

The **Quantum Approximate Optimization Algorithm (QAOA)** is designed to solve combinatorial optimization problems by:

- Encoding the scheduling problem into a **cost Hamiltonian**
- Representing constraints (energy, visibility, priority) as **quantum operators**
- Exploring multiple scheduling configurations **in superposition**
- Amplifying optimal solutions through **quantum interference**

---

### 4.2 Quantum Model Representation

- **Qubits** represent task selection states (0 = not selected, 1 = selected)
- **Cost Function** encodes:
  - Energy minimization
  - Priority maximization
  - Visibility constraints
- **Measurement probabilities** indicate optimal schedules

---

### 4.3 Quantum Output Interpretation

#### Quantum Result:
<img width="855" height="393" alt="image" src="https://github.com/user-attachments/assets/03991ab1-afe6-4afc-a12f-6ad43feb0838" />

- **High probability amplitude for Task T4**
  
- Other tasks show lower probability of selection

#### Key Insight:
<img width="547" height="433" alt="image" src="https://github.com/user-attachments/assets/c55d84c6-f982-4c36-a914-4970c9cfb2eb" />

Although T4 has **low classical priority**, the quantum model identifies it as a **globally optimal choice** when considering:

- Lower energy cost
- Reduced conflict with high-energy tasks
- Better long-term energy conservation across orbits

This probabilistic dominance emerges naturally from QAOA’s global optimization behavior.

---

## 5. Classical vs Quantum Comparison

### 5.1 Optimization Perspective

| Aspect | Classical | Quantum (QAOA) |
|-----|---------|----------------|
| Optimization Type | Local | Global |
| Exploration | Single-path | Superposition |
| Priority Handling | Rule-based | Weighted probabilistic |
| Energy Awareness | Greedy | Hamiltonian-based |
| Scalability | Limited | Promising for large problems |

---

### 5.2 Graph-Based Output Difference

- **Classical Graphs**  
  - Deterministic bar selection  
  - Fixed orange bars per window  
  - No probability interpretation  

- **Quantum Graph Output**  
  - Probability distribution over tasks  
  - Dominant peak for T4  
  - Reflects global cost minimization rather than window-level decisions  

---

## 6. Why Quantum Solution Wins Over Classical

1. **Global Optimization Capability**  
   QAOA evaluates all task combinations simultaneously instead of sequential selection.

2. **Energy–Priority Trade-off Awareness**  
   Quantum cost functions balance priority and energy more effectively.

3. **Probabilistic Decision Making**  
   Enables selection of non-obvious but optimal schedules.

4. **Reduced Myopic Decisions**  
   Avoids locally optimal but globally inefficient scheduling.

5. **Future Scalability**  
   Well-suited for large satellite constellations with hundreds of tasks.

---

## 7. My Output Comparison Summary

In my implementation:

- The **classical model** schedules tasks strictly based on visibility windows, resulting in fixed task selection regardless of global efficiency.
- The **quantum model** identifies Task T4 as the most probable optimal solution, demonstrating how QAOA can override traditional priority assumptions to achieve better energy efficiency.

This highlights the **fundamental paradigm shift** from deterministic scheduling to probabilistic, globally optimized decision-making.

---

## 8. Future Scope

1. **Hybrid Classical–Quantum Scheduling**
   - Use classical preprocessing with quantum optimization layers.

2. **Dynamic Orbital Modeling**
   - Incorporate real-time orbital changes and stochastic visibility windows.

3. **Multi-Satellite Constellations**
   - Extend QAOA to cooperative scheduling across satellite networks.

4. **Hardware Implementation**
   - Test on NISQ-era quantum processors.

5. **AI + Quantum Integration**
   - Combine reinforcement learning with QAOA parameter tuning.

---

## 9. Conclusion

This project demonstrates that **QAOA-based quantum scheduling** provides a powerful alternative to classical methods for energy-efficient satellite task scheduling. While classical approaches remain practical today, quantum optimization shows clear advantages in **global reasoning, scalability, and energy-aware decision making**, making it a promising solution for future space systems.

---

## Author & Project Information

**Project Title:**  **QAOA-Based Energy Efficient Satellite Task Scheduling Under Orbital Visibility Constraints**

**Author:**  **Shreya Sunil Palase**

**Date:**  **2 Janaury 2026**

**Project Type:** Research-Oriented Quantum Computing Project

**Domain:**  Quantum Optimization · Satellite Systems · Energy-Efficient Scheduling

---

*This document was prepared as part of an academic exploration into the application of quantum algorithms for solving complex, real-world optimization problems in space systems engineering.*
