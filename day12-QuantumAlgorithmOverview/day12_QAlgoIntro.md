# Introduction to Quantum Algorithms  
### Theory Notes with Prerequisites & Purpose of Key Algorithms  
Author: *Shreya Palase*  
Created: 5-Dec-2025  

---

# Table of Contents
- [1. Introduction to Quantum Algorithms](#1-introduction-to-quantum-algorithms)
- [2. Prerequisite Knowledge](#2-prerequisite-knowledge)
  - [2.1 Linear Algebra](#21-linear-algebra)
  - [2.2 Quantum Mechanics Basics](#22-quantum-mechanics-basics)
  - [2.3 Quantum Circuits](#23-quantum-circuits)
  - [2.4 Probability & Complex Numbers](#24-probability--complex-numbers)
- [3. Overview of Key Quantum Algorithms](#3-overview-of-key-quantum-algorithms)
  - [3.1 Deutsch–Jozsa Algorithm](#31-deutschjozsa-algorithm)
  - [3.2 Grover’s Algorithm](#32-grovers-algorithm)
  - [3.3 Variational Quantum Eigensolver (VQE)](#33-variational-quantum-eigensolver-vqe)
  - [3.4 Quantum Approximate Optimization Algorithm (QAOA)](#34-quantum-approximate-optimization-algorithm-qaoa)
  - [3.5 Quantum Phase Estimation (QPE)](#35-quantum-phase-estimation-qpe)
- [4. Summary Table](#4-summary-table)

---

# 1. Introduction to Quantum Algorithms

Quantum algorithms are computational procedures that run on quantum computers and leverage uniquely quantum phenomena—**superposition, entanglement, and interference**—to achieve speedups over classical computation.

Unlike classical algorithms that operate on bits (`0` and `1`), quantum algorithms use **qubits**, which can exist in a superposition of both 0 and 1 simultaneously. This ability allows quantum computers to process a large amount of information in parallel.

Quantum algorithms solve a wide variety of tasks:
- Speeding up search problems  
- Factoring large numbers  
- Simulating molecules  
- Solving optimization and machine-learning problems  
- Estimating eigenvalues of matrices  

This document introduces core quantum algorithms used in modern quantum computation.

---

# 2. Prerequisite Knowledge

Understanding quantum algorithms requires some prior background. Below are the essential topics.

---

## 2.1 Linear Algebra

You should be familiar with:

- Vectors and unit vectors  
- Inner products & orthogonality  
- Complex numbers  
- Matrices and matrix multiplication  
- Eigenvalues and eigenvectors  
- Tensor products  

Quantum states are represented as vectors (e.g., `|0⟩ = [1,0]ᵀ`), and quantum gates are unitary matrices.

---

## 2.2 Quantum Mechanics Basics

Important concepts:

- **Qubit** — quantum bit represented as  
  `|ψ⟩ = α|0⟩ + β|1⟩` with `|α|² + |β|² = 1`
- **Superposition** — states can exist in multiple configurations
- **Entanglement** — correlations stronger than classical physics
- **Measurement** — probabilistic collapse of the wavefunction

These principles directly affect quantum algorithms.

---

## 2.3 Quantum Circuits

Quantum algorithms are implemented via circuits composed of **quantum gates**.

Key gates:
- **H (Hadamard)**: creates superposition  
- **X (NOT)**: flips a qubit  
- **Z (phase flip)**  
- **CNOT**: controlled NOT  
- **U gates**: general single-qubit rotations  
- **Controlled-U gates**: apply `U` only if control qubit is `1`

Understanding the **Quantum Fourier Transform (QFT)** is important for advanced algorithms like QPE.

---

## 2.4 Probability & Complex Numbers

Quantum mechanics is deeply connected to probability:
- Amplitudes are complex numbers  
- Measurement probabilities are obtained by `|amplitude|²`  
- Interference can amplify or cancel outcomes  

---

# 3. Overview of Key Quantum Algorithms

The following sections describe the motivation, intuition, and purpose behind the major algorithms.

---

# 3.1 Deutsch–Jozsa Algorithm

### **Purpose**
To determine whether a function  
`f: {0,1}ⁿ → {0,1}`  
is **constant** or **balanced**, using **only one oracle query**.

### **Why It Matters**
Classically, in the worst case, you must evaluate the function `2^(n−1) + 1` times.  
Quantumly, you need just **one evaluation** due to superposition and interference.

### **Core Idea**
- Prepare all inputs simultaneously using Hadamard gates  
- Oracle evaluates `f(x)` for all `x` in parallel  
- Interference reveals the global property (constant or balanced)  

### **Use Cases**
- Demonstrates exponential quantum speedup  
- Foundation of the Hidden Subgroup Problem (HSP) family  

---

# 3.2 Grover’s Algorithm

### **Purpose**
To search an unsorted database of size `N` in  
**O(√N)** time instead of classical **O(N)**.

### **Why It Matters**
It gives a **quadratic speedup** for search — applicable to optimization, database lookup, and cryptanalysis.

### **Core Idea**
Uses two key operations:
- **Oracle**: marks the desired state by flipping its phase  
- **Diffusion operator**: amplifies the probability of the marked state  

Each iteration increases the probability of the correct answer.

### **Use Cases**
- Unstructured search  
- NP optimization problems  
- Speedups in machine learning  

---

# 3.3 Variational Quantum Eigensolver (VQE)

### **Purpose**
To compute the **ground-state energy** of molecules or Hamiltonians using a hybrid quantum–classical method.

### **Why It Matters**
It is one of the most promising algorithms for Noisy Intermediate-Scale Quantum (NISQ) devices.

### **Core Idea**
1. Choose a parameterized circuit (ansatz)  
2. Prepare quantum state `|ψ(θ)⟩`  
3. Measure expectation values of Hamiltonian terms  
4. Classical optimizer updates parameters  

### **Use Cases**
- Quantum chemistry  
- Material science  
- Finding low-energy quantum states  
- Useful on today's NISQ hardware  

---

# 3.4 Quantum Approximate Optimization Algorithm (QAOA)

### **Purpose**
To solve **combinatorial optimization problems** (e.g., MaxCut) using a variational approach.

### **Why It Matters**
QAOA is considered a leading candidate for quantum advantage in optimization and machine learning.

### **Core Idea**
Alternate between:
- **Cost Hamiltonian** (`U_C`): encodes objective function  
- **Mixer Hamiltonian** (`U_B`): explores solution space  

The parameters `(β, γ)` are optimized classically.

### **Use Cases**
- MaxCut  
- Traveling Salesman variants  
- Graph partitioning  
- Constraint-satisfaction problems  

---

# 3.5 Quantum Phase Estimation (QPE)

### **Purpose**
To estimate the phase `φ` in the eigenvalue equation:

`U |ψ⟩ = e^{2πiφ} |ψ⟩`

### **Why It Matters**
QPE is one of the **most important algorithms** in all of quantum computing.  
It is the core of:
- Shor’s factoring algorithm  
- Quantum chemistry simulations  
- Some Hamiltonian simulation algorithms  

### **Core Idea**
1. Use superposition of time steps  
2. Apply powers of the unitary (`U`, `U²`, `U⁴`, …)  
3. Use the inverse QFT to recover phase  

### **Use Cases**
- Eigenvalue estimation  
- Factoring large integers  
- Quantum simulations  
- Solving linear systems (HHL)  

---

# 4. Summary Table

| Algorithm | Purpose | Complexity | Use Cases |
|----------|---------|------------|-----------|
| **Deutsch–Jozsa** | Determine if a function is constant or balanced | 1 query quantum vs. exponential classical | Demonstrates quantum advantage |
| **Grover’s Algorithm** | Search an unsorted list | O(√N) | Search, optimization, ML |
| **VQE** | Ground-state energy estimation | Hybrid classical/quantum | Chemistry, materials |
| **QAOA** | Approximation for combinatorial optimization | Hybrid; depth p | MaxCut, graph problems |
| **QPE** | Estimate eigenvalues of unitary operators | O(n²) gates | Shor, chemistry, simulation |

---


