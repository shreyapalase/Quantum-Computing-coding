# 🚀 QAOA-Based Energy-Efficient Satellite Task Scheduling Under Orbital Visibility Constraint

---

## 🌟 Project Purpose

Satellite operations involve scheduling multiple observation and communication tasks while respecting **limited energy resources**, **orbital visibility constraints**, and **task priorities**. Efficient scheduling is critical for maximizing the value of each satellite mission while avoiding conflicts and energy wastage.  

This project aims to **leverage quantum computing**, specifically the **Quantum Approximate Optimization Algorithm (QAOA)**, to optimize satellite task scheduling, providing high-quality solutions that are challenging for classical methods.

---

## 🧩 Problem Statement

Traditional satellite task scheduling is a **combinatorial optimization problem**. Key challenges include:

- **Limited energy budget:** Each satellite has a finite battery capacity.  
- **Visibility windows:** Tasks can only be executed when the satellite is in the correct orbital position.  
- **Task priorities:** Some tasks are more critical than others, e.g., emergency Earth imaging or high-priority scientific experiments.  
- **Time conflicts:** Overlapping tasks cannot be executed simultaneously if they share the same window.

Classical optimization algorithms struggle as the number of tasks, satellites, and constraints increase, making the problem computationally expensive and sometimes intractable.

---

## ⚛ Why Quantum Optimization (QAOA)?

The **Quantum Approximate Optimization Algorithm (QAOA)** is a **hybrid quantum-classical algorithm** that excels in combinatorial optimization problems. Its advantages over classical methods include:

- **Natural representation of binary decisions:** Each task can be encoded as a binary variable (executed or skipped).  
- **Efficient exploration of solution space:** Quantum superposition and entanglement allow simultaneous exploration of multiple schedules.  
- **Potential to find better approximations faster:** Especially valuable for large-scale satellite missions with tight energy and visibility constraints.

QAOA offers a **promising alternative** to classical optimization, providing a path toward **energy-efficient and conflict-free satellite scheduling**.

---

## 🛠 Project Goals

In this project, we aim to:

1. Formulate the satellite task scheduling problem in terms of **binary decision variables**.  
2. Define **energy, visibility, and priority constraints** clearly.  
3. Develop a **QAOA-based quantum optimization model** for efficient scheduling.  
4. Evaluate the algorithm’s performance using **simulators** like Qiskit AER.  

---

## 📝 Researcher & Project Info

**Author / Researcher:**  
👉 *Shreya Sunil Palase* — *Quantum Computing Independent Researcher / Student*

**Date Created:**  
📅 30 December 2025

---

## 🚨 Copyright, Security & Usage Declaration

⚠️ **Security Notice:**  
This project—including all codes, research ideas, formulations, and documentation—is **intellectual property of the author**.  

**Strictly prohibited actions without written permission from the author:**  
- Copying or replicating any part of the project.  
- Redistributing or publishing the project materials.  
- Using the project for commercial purposes.  

Any unauthorized access, usage, or reproduction will be considered a violation of intellectual property rights.  
This project is intended solely for **academic, research, and educational purposes**.

- Shreya Palase(codeQubit)
 
