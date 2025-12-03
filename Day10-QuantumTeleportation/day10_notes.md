# Day10 Notes- Quantum Teleportation 

Quantum Teleportation is a protocol that allows the transfer of an **unknown quantum state** from one qubit (held by **Alice**) to another qubit (held by **Bob**) **without physically sending the qubit itself**.  
It exploits two essential resources: **quantum entanglement** and **classical communication**.

---

## 🧠 1. Core Idea Behind Quantum Teleportation

Suppose Alice has a qubit in an **unknown state**:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

Alice wants Bob to obtain *exactly this state*, but she cannot simply measure and send the result—because measurement collapses the state.

Quantum Teleportation lets Alice send this state to Bob *perfectly* using:

1. A shared entangled pair (Bell state)  
2. Classical communication (2 bits)  
3. Conditional unitary operations by Bob  

Importantly, the state **disappears** from Alice’s side when Bob reconstructs it — avoiding violation of the no-cloning theorem.

---

## 🔗 2. Requirements for Teleportation

### ✔ **1. Entanglement**

Alice and Bob share a maximally entangled pair:

$$
|\phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

- Alice receives qubit **A₂**  
- Bob receives qubit **B**

The state to be teleported is **A₁**.

So initially:

$$
|\psi\rangle_{A_1} \otimes |\phi^+\rangle_{A_2 B}
$$

---

### ✔ **2. Classical Communication — 2 Bits**

After locally interacting her two qubits (**A₁**, **A₂**) and measuring them,  
Alice obtains **2 classical bits** (00, 01, 10, or 11).

She sends these 2 bits to Bob using classical channels (phone, internet, etc.).

---

### ✔ **3. Conditional Operations (Performed by Bob)**

Depending on Alice’s 2-bit message, Bob applies appropriate corrections:

| Alice’s Bits | Bob Applies |
|--------------|-------------|
| 00           | Identity (I) |
| 01           | X gate |
| 10           | Z gate |
| 11           | ZX (or XZ) |

These operations transform Bob’s qubit into the original state:

$$
|\psi\rangle_B = \alpha|0\rangle + \beta|1\rangle
$$

Bob has now perfectly reconstructed the unknown state.

---

## 🔄 3. Steps of the Teleportation Protocol

### **Step 1 — Share Entanglement**
Bob and Alice share a Bell pair created beforehand.

### **Step 2 — Alice Entangles Her Qubits**

Alice applies:
- **CNOT** from A₁ → A₂  
- **Hadamard (H)** on A₁

This mixes the unknown state with her half of the Bell pair.

### **Step 3 — Alice Measures Her Qubits**

Measurement outputs two classical bits.

### **Step 4 — Send Classical Bits**

Alice transmits the two bits to Bob.

### **Step 5 — Bob Applies Correction**

Bob performs I, X, Z, or ZX accordingly.

Result:  
Bob's qubit becomes **exactly** the original unknown quantum state.

---

## 🧪 4. What We Will Do in the Notebook

In the upcoming notebook, we will:

1. **Understand the theory behind the teleportation.**  
   - Review entanglement, Bell states, quantum state evolution.

2. **Build the teleportation circuit in Qiskit.**  
   - Step-by-step construction of the protocol.

3. **Visualize intermediate quantum states.**  
   - Bloch spheres  
   - Statevector representations  
   - Circuit snapshots  

4. **Verify the correctness.**  
   - Confirm that Bob’s final state matches the original unknown state.

---

## 📎 Summary

Quantum teleportation does **not** transmit matter or energy faster than light.  
Instead, it transfers **information about a quantum state** using:

- Shared entanglement  
- Local quantum operations  
- Two classical bits  
- Conditional unitaries  

This protocol is fundamental in:
- Quantum networks  
- Distributed quantum computing  
- Quantum repeaters  

---

This is theory notes for understanding Quantum computing Teleporation concept.for practical refer file **day10_QuantumTeleportation.ipynb**.

---

**Written By**: Shreya Palase

**Date** : 3-Dec-2025

Thank you and Keep Learning!
