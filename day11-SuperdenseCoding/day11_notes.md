# day 11 Notes - Superdense Coding in Quantum Computing


Superdense coding is a fundamental quantum information concept that reveals how **quantum entanglement increases classical communication capacity** beyond what is possible in any classical theory. It is one of the earliest examples demonstrating that quantum systems do not merely replace classical communication lines but can **strengthen** them through nonclassical correlations.

This document focuses purely on the conceptual and theoretical meaning of superdense coding, without implementation steps or protocol instructions.

---

## 1. What Superdense Coding Is (Conceptual View)

Superdense coding is a communication phenomenon in which **two classical bits can be transmitted by sending only one qubit**, provided the communicating parties initially share a pair of entangled qubits.

The important insight is that the increased communication capacity does **not** originate from the qubit being physically capable of "holding more information."  
Instead, it arises because:

1. **Entanglement creates a joint quantum state with larger structure and distinguishability** than either qubit possesses individually.
2. **Local operations on one qubit affect the global state**, even though the operation is performed locally.
3. **The receiver, who ultimately has access to both qubits**, can extract more classical information from the joint system than can be encoded in a single isolated qubit.

Thus, superdense coding is not about packing extra information *into* a qubit, but about exploiting the **latent informational capacity of an entangled system**.

---

## 2. Entanglement as an Information Resource

Classically, communication capacity is tied to the physical medium carrying the signal.  
Quantum mechanically, entanglement changes this relationship.

A maximally entangled pair of qubits spans a **four-dimensional Hilbert space**, meaning it can exist in one of **four orthogonal states**. These states are the Bell states:

$$
|\Phi^{+}\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

$$
|\Phi^{-}\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

$$
|\Psi^{+}\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}
$$

$$
|\Psi^{-}\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

These four states are **mutually orthogonal**, meaning they are as distinguishable as possible.

When two parties (Alice and Bob) share a Bell state:

- The **entangled pair** collectively contains the capacity to encode four classical possibilities.
- Each qubit individually appears maximally mixed and carries no useful information on its own.
- The informational capacity is stored **nonlocally**, in the correlations.

This is the core theoretical insight:  
**Quantum information can reside in correlations, not in the individual systems.**

---

## 3. Local Transformations and Global Distinguishability

A central principle behind superdense coding is:

**Local quantum operations can transform a shared entangled state into a different global state.**

If Alice has one qubit of the entangled pair, then by acting only on her qubit, she can generate all four Bell states. The reason this is possible is that the entangled state is a **global object**. Changing part of it changes the whole.

This highlights a profound theoretical feature:

- **Entanglement allows global state manipulation from local actions.**
- The local system contains no classical information.
- But the pair, as a whole, does.

Thus, even though Alice’s qubit by itself appears to contain *zero* classical bits (it is maximally mixed), her ability to choose among several transformations of the **entangled pair** gives her access to a higher-dimensional information space.

This is the key to understanding how a single qubit can enable the communication of two classical bits.

---

## 4. Why the Receiver Can Recover More Information Than Was Sent

Bob ultimately receives Alice’s qubit, but crucially, he already possesses his part of the entangled pair.

This means Bob holds:

- **one qubit that traveled from Alice**, and  
- **one qubit that was pre-shared**.

Together, these form a two-qubit system whose state Alice has effectively chosen.

Because the four Bell states are orthogonal, Bob can, in principle, perform a measurement that distinguishes them perfectly. Each Bell state corresponds to one of four classical outcomes, i.e., two classical bits.

Thus, even though Alice physically transmitted only one qubit, Bob’s measurement acts on a **two-qubit quantum system**, allowing him to extract more classical information than is contained in a single transmitted particle.

In classical communication theory, this seems impossible — but in quantum theory, the receiver’s access to previously entangled resources fundamentally changes what is possible.

---

## 5. What Superdense Coding Tells Us About Quantum Information

Superdense coding is not merely a communication trick; it reveals foundational truths about quantum information:

### 5.1 Information Can Be Stored in Correlations
In classical systems, correlations do not hold information beyond what is contained in each component.  
But in quantum systems, entanglement holds **additional, nonlocal information**.

### 5.2 Classical Capacity Is Enhanced by Quantum Resources
Even classical bits can be communicated more efficiently using quantum correlations.  
This demonstrates that communication capacity is not a fixed quantity of the physical medium, but can be **augmented by entanglement**.

### 5.3 Local Actions Have Nonlocal Consequences
This does not violate relativity because the entanglement cannot be used alone to send signals.  
However, once classical communication occurs (such as sending one qubit), the latent nonlocal structure becomes observable.

### 5.4 Entanglement Is a Consumable Resource
Once superdense coding is performed and Bob measures the state, the entanglement is destroyed.  
This shows that entanglement behaves like a **valuable resource** in quantum information theory — something that must be created, shared, consumed, and replenished.

---

## 6. Theoretical Meaning in Quantum Information Science

Superdense coding is often seen as the communication-theoretic counterpart to quantum teleportation.  
Where teleportation transfers a quantum state using classical bits and pre-shared entanglement, superdense coding transfers classical bits using a qubit and pre-shared entanglement.

This duality reveals a deeper theoretical structure:

- **Entanglement + classical communication = quantum state transfer**  
- **Entanglement + quantum communication = enhanced classical state transfer**

These relationships form the backbone of modern quantum information theory.

Superdense coding thereby illustrates that communication itself becomes **programmable through entanglement** — something impossible in classical physics.

---

---

# Superdense Coding — Practical Explaination (Qunatum coding)

---

---


## 1. Introduction

Superdense coding demonstrates how **entanglement functions as a communication resource**, enabling a single transmitted qubit to effectively carry two classical bits. The key steps are:

1. Alice and Bob share an entangled pair.
2. Alice applies one of four operations to encode her 2-bit message.
3. Alice sends her qubit to Bob.
4. Bob performs a Bell-state measurement to decode the 2-bit message.

---

## 2. Theory Behind Superdense Coding

Before communication, Alice and Bob share the Bell state:

$$
|\Phi^{+}\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

Bob keeps one qubit, and Alice keeps the other.

### 2.1 Local Operation, Global Effects

Entanglement has the property that **local operations on one qubit change the global joint state**.  
Alice can choose one of four unitary operations on her qubit:

$$
I,\; X,\; Z,\; XZ
$$

Each transforms the shared state into a distinct and orthogonal Bell state.

---

## 3. How Entanglement Enables 2 Bits per Transmitted Qubit

A single unentangled qubit can encode at most **1 classical bit**, because any measurement yields one of two outcomes.

But with entanglement:

- The joint 2-qubit system spans a **4-dimensional** Hilbert space.
- Alice, by acting only on her qubit, can steer the global state into one of **4 distinct Bell states**.
- Each Bell state corresponds to **2 classical bits**.

Thus:

$$
1\ \text{transmitted qubit (with shared entanglement)} \rightarrow 2\ \text{classical bits}
$$

This does not violate relativity because entanglement alone does not carry information — communication still requires transmitting Alice’s qubit.

---

## 4. Mapping the 2-Bit Message to Quantum Gates

Alice wants to send a 2-bit message:

$$
b_1 b_0 \in \{00,\;01,\;10,\;11\}
$$

She applies one of the following operations:                                        

| Classical bits | Gate applied | Resulting Bell state  |
|----------------|--------------|-----------------------|
| 00             | I            | \|Φ+> → \|00>           |
| 01             | X            | \|Ψ+> → \|01>           |
| 10             | Z            | \|Φ-> → \|10>           |
| 11             | XZ           | \|Ψ-> → \|11>           |

The four Bell states are:

$$
|\Phi^{+}\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

$$
|\Phi^{-}\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

$$
|\Psi^{+}\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}
$$

$$
|\Psi^{-}\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

Alice now sends *her single qubit* to Bob.

---

## 5. Bob’s Decoding Procedure

Once Bob receives Alice’s qubit, he possesses both qubits of the entangled pair.

To recover the message, Bob transforms the Bell states back into computational basis states.

### Step 1 — Apply CNOT

Control qubit: Bob’s original qubit  
Target qubit: Alice’s qubit

### Step 2 — Apply Hadamard to Bob’s qubit

This operation maps:

$$
|\Phi^{+}\rangle \rightarrow |00\rangle
$$

$$
|\Psi^{+}\rangle \rightarrow |01\rangle
$$

$$
|\Phi^{-}\rangle \rightarrow |10\rangle
$$

$$
|\Psi^{-}\rangle \rightarrow |11\rangle
$$

### Step 3 — Measure both qubits

The measurement yields exactly the 2 classical bits that Alice encoded.

---

## 6. Full Superdense Coding Algorithm

### **Pre-shared entanglement**
1. Alice and Bob prepare the entangled state:

$$
|\Phi^{+}\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

### **Alice's encoding**
2. Alice selects a 2-bit message (b1 b0).  
3. She applies the gate:

   - I for 00  
   - X for 01  
   - Z for 10  
   - XZ for 11  

4. Alice sends her qubit to Bob.

### **Bob’s decoding**
5. Bob now holds two qubits.  
6. He applies the CNOT gate.  
7. He applies the Hadamard gate.  
8. He measures both qubits.  
9. The measurement result is the classical message:

$$
00,\; 01,\; 10,\; 11
$$

---

## 7. Summary

- Superdense coding allows a single transmitted qubit to carry two classical bits.
- The protocol relies on the ability of entanglement to encode four distinguishable joint states.
- Alice encodes using I, X, Z, or XZ.
- Bob decodes using CNOT + Hadamard + measurement.
- The enhanced capacity comes from pre-shared entanglement, not faster-than-light communication.

---

##  Conclusion

- A maximally entangled pair spans a 4-state space.
- Local operations on one qubit allow selection among these four global states.
- Sending one qubit enables the receiver to access a two-qubit system.
- The receiver can discriminate four orthogonal states, yielding two classical bits.
- No extra information rides on the transmitted qubit; the capacity comes from the **shared entanglement**.
- The protocol reveals that information in quantum mechanics can be **nonlocal**, **correlational**, and **resource-based**.

Superdense coding is therefore a profound theoretical statement:  
**Entanglement increases the classical communication capacity of quantum systems by allowing information to reside in correlations rather than in local states.**

---

**Written By:** Shreya Palase

**Date**: 4-Dec-2025

Thank you and Keep learning!

