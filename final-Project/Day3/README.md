# Day 3 – QAOA-Based Satellite Task Scheduling

## Overview
This repository documents **Day 3 progress** of the project on **Energy-Efficient Satellite Task Scheduling using QAOA under Orbital Visibility Constraints**.  
The focus of this stage is **problem modeling and interpretation**, explaining *why constraint-aware optimization leads to Task T4 having the highest selection probability*, even though other tasks have higher nominal priority.

The work emphasizes **conceptual clarity, engineering reasoning, and interview readiness**, rather than low-level quantum computation details.

---

## Project Files

### 📓 `QAOA_satellite_Schedulaer.ipynb`
Implements the QAOA-based task scheduling model, including objective formulation, constraint penalties, and interpretation of probabilistic outcomes.

### 📄 `quantum_baseline.md`
Provides a concise theoretical baseline explaining QAOA principles, constraint encoding strategy, and comparison with classical optimization approaches.

---

## Key Concepts Covered
- Constraint-aware optimization vs greedy priority selection  
- Energy budget enforcement using penalty modeling  
- Orbital visibility conflict handling  
- Interpretation of probabilistic outputs in QAOA  
- Engineering justification for Task T4 dominance  

---

## Related Research Papers (arXiv)

The following research papers provide foundational and implementation-level insights into QAOA and quantum optimization:

1. **Farhi et al. – A Quantum Approximate Optimization Algorithm**  
   https://arxiv.org/abs/1411.4028

2. **Hadfield et al. – From the Quantum Approximate Optimization Algorithm to a Quantum Alternating Operator Ansatz**  
   https://arxiv.org/abs/1709.03489

3. **Egger et al. – Quantum Computing for Finance and Optimization**  
   https://arxiv.org/abs/1903.03044

4. **Barkoutsos et al. – Improving Variational Quantum Optimization using CVaR**  
   https://arxiv.org/abs/1907.04769

---

## Security & Academic Integrity Notice

⚠️ **Usage Policy**
- This project is intended for **educational and research purposes only**
- Direct copying or rebranding of this work for academic submission or commercial use is **strictly discouraged**
- Proper citation and acknowledgment are required if concepts or structures are reused

🔐 **Original Work Statement**
All problem formulations, interpretations, and explanations reflect **independent analytical work** and are structured specifically for learning, interviews, and research discussion.

---

## Status
✔ Day 3 – Problem Modeling & Interpretation Complete  
⏳ Next: Result visualization and comparative analysis

---
