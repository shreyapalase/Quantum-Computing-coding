# Day26 notes - Quantum Cryptography

## Introduction

Quantum Cryptography is a modern cryptographic approach that leverages the **laws of quantum mechanics** to enable **secure communication**. Unlike classical cryptography, whose security relies on computational hardness assumptions, quantum cryptography provides **information-theoretic security**, meaning security guaranteed by the fundamental laws of physics.

The most widely used application of quantum cryptography is **Quantum Key Distribution (QKD)**, which allows two parties to generate a shared, secret encryption key while detecting any eavesdropping attempt.

---

## What is Quantum Cryptography?

Quantum Cryptography refers to cryptographic techniques that utilize **quantum states**, such as photons, to perform cryptographic tasks. Its core principle is that **measuring a quantum system disturbs it**, making unauthorized interception detectable.

### Key Characteristics

- Based on **quantum mechanics**, not mathematical complexity  
- Guarantees **eavesdropper detection**  
- Provides **unconditional security**  
- Resistant to **quantum computer attacks**

Quantum cryptography does **not** replace classical encryption algorithms like AES or RSA. Instead, it **securely distributes encryption keys**, which are later used with classical cryptographic algorithms.

---

## Why Classical Cryptography is Vulnerable?

Classical cryptographic systems rely on problems that are **hard to solve computationally**, but not impossible.

### 1. Dependence on Computational Hardness

Classical cryptography assumes that certain mathematical problems are infeasible to solve:

- RSA → Integer Factorization  
- ECC → Discrete Logarithm Problem  

However, these problems are **not proven unsolvable**, only difficult with current classical computers.

---

### 2. Threat of Quantum Computers

Quantum algorithms significantly weaken classical cryptography:

- **Shor’s Algorithm** can factor large integers in polynomial time  

$$
\text{RSA Security} \xrightarrow{\text{Shor's Algorithm}} \text{Broken}
$$

This means future quantum computers can **break widely-used cryptosystems**.

---

### 3. Undetectable Eavesdropping

In classical communication:

- Data can be copied  
- Eavesdropping leaves **no trace**  
- Man-in-the-middle attacks are hard to detect  

Quantum cryptography overcomes this limitation.

---

## Core Idea of Quantum Key Distribution (QKD)

Quantum Key Distribution enables two parties—traditionally called **Alice** (sender) and **Bob** (receiver)—to generate a **shared random secret key** using quantum states.

### Fundamental Quantum Principles Used

#### 1. Superposition

A quantum bit (qubit) can exist in multiple states simultaneously:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

where

$$
|\alpha|^2 + |\beta|^2 = 1
$$

---

#### 2. Measurement Disturbance

Measuring a quantum state **collapses** it into a definite value, permanently altering the state.

---

#### 3. No-Cloning Theorem

It is **impossible to copy an unknown quantum state**:

$$
|\psi\rangle \nrightarrow |\psi\rangle |\psi\rangle
$$

This prevents an eavesdropper from secretly duplicating transmitted qubits.

---

### Security Insight

If an eavesdropper (Eve) tries to measure qubits:

- Errors are introduced  
- Alice and Bob detect anomalies  
- The communication is aborted  

---

## Quantum Key Distribution Workflow

1. Alice sends qubits encoded in random bases  
2. Bob measures using random bases  
3. Alice and Bob compare bases over a classical channel  
4. Mismatched measurements are discarded  
5. Remaining bits form the **secret key**  
6. Errors indicate eavesdropping  

---

## BB84 Protocol

The **BB84 protocol**, proposed by **Bennett and Brassard (1984)**, is the first and most famous QKD protocol.

### Encoding Scheme

BB84 uses **two bases**:

#### 1. Rectilinear Basis (+)

- |0⟩ → Horizontal (0)  
- |1⟩ → Vertical (1)  

#### 2. Diagonal Basis (×)

- |+⟩ → 45° (0)  
- |−⟩ → 135° (1)  

---

### BB84 States Representation

$$
\begin{aligned}
|0\rangle &= \begin{bmatrix}1 \\ 0\end{bmatrix} \\
|1\rangle &= \begin{bmatrix}0 \\ 1\end{bmatrix} \\
|+\rangle &= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \\
|-\rangle &= \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
\end{aligned}
$$

---

## BB84 Protocol Steps

### Step 1: Key Encoding (Alice)

- Alice generates a random bit string  
- She randomly selects a basis (+ or ×)  
- Encodes each bit into a qubit  

---

### Step 2: Transmission

- Alice sends qubits through a quantum channel  
- Eve cannot copy or measure without disturbance  

---

### Step 3: Measurement (Bob)

- Bob randomly chooses a basis for each qubit  
- Measures and records results  

---

### Step 4: Basis Reconciliation

- Alice and Bob publicly compare bases  
- Bits with matching bases are kept  
- Others are discarded  

---

### Step 5: Eavesdropping Detection

- A subset of bits is compared  
- Error rate above threshold → eavesdropping detected  

$$
\text{High Error Rate} \Rightarrow \text{Eve Detected}
$$

---

### Step 6: Key Generation

- Remaining bits form the **secure shared key**  
- Used for classical encryption (e.g., AES)  

---

## Security of BB84 Protocol

BB84 is secure because:

- Measurement changes quantum states  
- Eve introduces detectable errors  
- No-cloning theorem prevents perfect interception  

Even with unlimited computational power, Eve **cannot extract information without being detected**.

---

## Implementing BB84 Using Qiskit and AerSimulator (Conceptual Overview)

In quantum simulation frameworks like **Qiskit**, BB84 is implemented using:

- Qubits to represent photons  
- Quantum gates for basis preparation  
- Measurements to simulate Bob’s detection  
- AerSimulator to emulate quantum noise and behavior  

The simulator allows:

- Controlled experiments  
- Error analysis  
- Visualization of quantum security principles  

---

## Summary

- Classical cryptography is vulnerable to quantum attacks  
- Quantum cryptography provides physics-based security  
- QKD ensures secure key exchange  
- BB84 is the foundational QKD protocol  
- Security arises from quantum measurement laws  
- Qiskit enables realistic quantum cryptography simulations  

---

## Final Insight

> **Quantum Cryptography shifts security from "hard to compute" to "impossible to violate without detection".**

This paradigm is essential for securing future communication systems in the quantum era.

---

**Written By** : Shreya Palase

**Date** : 20-Dec-2025

Thank you and keep learning!
