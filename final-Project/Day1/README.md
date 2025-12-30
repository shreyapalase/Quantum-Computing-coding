# QAOA-Based Energy-Efficient Satellite Task Scheduling Under Orbital Visibility Constraints
This Folder contain working of Day1 with research material ,problem definition from scratch.Seperate markdown file for each step we will perform in our project.

---

## 📌 Project Overview

This project investigates the application of **quantum optimization**, specifically the **Quantum Approximate Optimization Algorithm (QAOA)**, to solve the **satellite task scheduling problem** under realistic operational constraints.

Satellite missions operate in highly constrained environments with limited energy, strict orbital visibility windows, and competing task priorities. Efficient scheduling is critical for maximizing mission value and extending satellite lifespan.  
This work formulates the scheduling problem as a **binary optimization problem** and prepares it for solution using **quantum algorithms**.

---

## 🚀 Problem Motivation

Modern satellites are required to perform multiple tasks such as:
- Earth observation
- Weather sensing
- Ground communication
- Scientific experiments

However, they face severe limitations:
- **Limited battery energy**
- **Short and overlapping visibility windows**
- **Single-task execution capability**
- **Mission-critical priority constraints**

Traditional scheduling methods struggle as the problem size and complexity grow. This motivates the exploration of **quantum optimization techniques** that are naturally suited for **combinatorial decision-making problems**.

---

## ❓ Why Quantum Optimization?

The satellite task scheduling problem is:
- Combinatorial
- Constraint-heavy
- NP-hard in nature

### Advantages of Quantum Optimization (QAOA)

- Naturally handles **binary decision variables**
- Encodes constraints as **penalty terms**
- Suitable for **QUBO and Ising formulations**
- Promising scalability for large task sets
- Hybrid quantum–classical adaptability

QAOA provides a principled framework to explore high-quality solutions for complex scheduling problems beyond classical heuristics.

---

## 🛠 Tools & Technologies Used

- **Qiskit** – Quantum algorithm design and implementation  
- **Qiskit Aer Simulator** – Classical simulation of quantum circuits  
- **Python** – Modeling and experimentation  
- **Markdown** – Research documentation  

---

## 📂 Project Structure & Research Workflow

This repository follows a **step-by-step research pipeline**, where each Markdown file represents a key modeling stage.

### 🔹 Step-by-Step Breakdown

| Step | File Name | Description |
|----|---------|-------------|
| Step 1 | `Step1_Satelite_Mission_Overview.md` | Understanding real satellite operations, tasks, energy limits, and visibility constraints |
| Step 2 | `Step2_problem_formulation.md` | Defining a simplified but realistic mission scenario with tasks, energy costs, and visibility windows |
| Step 3 | `Step3_Binary_Decision_Variables.md` | Introducing binary decision variables and explaining why they fit quantum optimization |
| Step 4 | `Step4_constraint_Model.md` | Deep explanation of energy, visibility, and mandatory task constraints |
| Step 5 | `Step5_optimization_objective.md` | Defining the optimization objective using reward and penalty terms |

---

## 🎯 Research Contributions

- Realistic modeling of satellite task scheduling constraints
- Clear binary formulation suitable for quantum optimization
- Reward–penalty based objective design
- QAOA-ready problem structure
- Educational, step-by-step research documentation

---
## 📚 Research Links (Key References)

### ✅ **Quantum Optimization & QAOA**
1. *Quantum Approximate Optimization with Hard and Soft Constraints* — NASA Technical Reports discussing QAOA circuit design in constrained problems. :contentReference[oaicite:2]{index=2}  
   **🔗** https://ntrs.nasa.gov/citations/20190029089

2. *QTIS: A QAOA-Based Quantum Time Interval Scheduler* — QAOA for scheduling with overlapping constraints — ArXiv. :contentReference[oaicite:3]{index=3}  
   **🔗** https://arxiv.org/abs/2511.15590

3. *A Hybrid Classical-Quantum Approach to Satellite Mission Planning* — ArXiv showing QAOA/VQE usage in satellite planning. :contentReference[oaicite:4]{index=4}  
   **🔗** https://arxiv.org/abs/2308.00029

---

### 🚀 **Real Satellite Missions (Context)**

1. **NASA-ISRO Synthetic Aperture Radar (NISAR)** — Joint Earth observation mission monitoring land and ice dynamics. :contentReference[oaicite:5]{index=5}  
   **🔗** https://acceleron.org.in/index.php/aaj/article/view/184

2. **NASA Partnership with ISRO** — NISAR mission objectives and partnership background. :contentReference[oaicite:6]{index=6}  
   **🔗** https://science.nasa.gov/mission/nisar/isro-partnership/
---

## 🚨 Security & Usage Declaration

⚠️ **IMPORTANT:**  
This project content — including conceptual designs, optimization formulations, and research discussions — is intended primarily

## 👤 Author Information

**Author:** *Shreya Sunil Palase(codeQubit)*  

**Role:** Independent Researcher 

**Project Focus:** Quantum Computing & Optimization 

**Date Created:** 30 December 2025  

---

## ⚠️ Research & Usage Declaration

This repository contains **original research documentation, problem formulations, and explanations** created solely for academic and educational purposes.

### Usage Policy
- ❌ Unauthorized copying or redistribution of this material is prohibited  
- ❌ Commercial use without explicit permission is not allowed  
- ✅ Referencing with proper citation is permitted for academic use  

If you wish to use or extend this work, please contact the author.

---

## 📬 Contact

For research collaboration, questions, or discussions related to:
- Quantum optimization
- Satellite scheduling
- QAOA modeling

Please reach out via GitHub Issues or repository contact details.

---

⭐ *If you find this project useful, consider starring the repository!*  
