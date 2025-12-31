### Day 2  
## QAOA-Based Energy-Efficient Satellite Task Scheduling Under Orbital Visibility Constraints

---

## Introduction

The **Day 2** folder contains the theoretical and research groundwork necessary to extend the satellite task scheduling problem from a **classical solution** to a **quantum optimization approach using QAOA**.  
All work is organized in **separate Markdown files**, clearly documenting each phase of the research and modeling process.

---

## Day 2 Goal (Short)

> **Formulate the satellite task scheduling problem into QUBO and Ising models suitable for QAOA, validated against the classical benchmark.**

---

## Classical Baseline Reference (Day 1)

The classical baseline provides the **optimal reference solution** under energy, priority, and visibility constraints, and is used throughout Day 2 for validation and comparison.

🔗 **Classical Baseline File:**  
`../Day1/Step2_problem_formation.md`

---
## Classical Baseline Files in This Project

This project includes the following classical scheduling artifacts used for validation and benchmarking:

- **`classical_result.md`**  
  Documents the final classical scheduling outcomes and optimal task selections per visibility window.

- **`classical_satellite_scheduler.py`**  
  Python implementation of the classical energy- and priority-aware satellite task scheduling algorithm.

- **`classical_baseline.ipynb`**  
  Interactive notebook demonstrating exhaustive search, cost evaluation, and result visualization for the classical baseline.

  ---


## Related Research Papers (Classical Satellite Scheduling)


### 1. An Energy-Efficient Learning Solution for the Agile Earth Observation Satellite Scheduling Problem
- Focus: Energy-aware scheduling with time and visibility constraints using learning-based optimization.  
- [arXiv Link](https://arxiv.org/abs/2503.04803)

---

### 2. Earth Observation Satellite Scheduling with Neural Methods
- Focus: Uses graph learning techniques to optimize scheduling considering visibility windows and weighted task selection.  
- [arXiv Link](https://arxiv.org/abs/2408.15041)

---

### 3. Safe Hierarchical Reinforcement Learning for CubeSat Task Scheduling Based on Energy Consumption
- Focus: Task scheduling for CubeSats with energy consumption constraints.  
- [arXiv Link](https://arxiv.org/abs/2309.12004)

---

### 4. In-Orbit Processing or Not? Sunlight-Aware Task Scheduling for Energy-Efficient Space Edge Computing Networks
- Focus: Energy-aware scheduling optimization in space edge computing environments.  
- [arXiv Link](https://arxiv.org/abs/2407.07337)

---

**Note:**  
These papers provide **open-access references** and theoretical foundations related to classical baseline satellite task scheduling and energy-priority optimization.


---

## Security & Academic Integrity

⚠️ **Important Notice**

- This repository is intended for **research and educational use only**
- **Do NOT copy or reuse code or content directly** for:
  - Academic assignments or exams
  - Publications without proper citation
- Any reuse of ideas, algorithms, or models must include appropriate attribution
- Unauthorized redistribution or plagiarism is strictly prohibited

This project adheres to **academic integrity and responsible research practices**.

---

