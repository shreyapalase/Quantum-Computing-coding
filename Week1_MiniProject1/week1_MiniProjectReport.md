# Mini Project Report
----

**Project Name** : Quantum Entanglement and Bell state

**Aim** : Bulid a Quantum State Circuit & Prove Entanglment by Correlated Measurement Results.

**Author**: Shreya Palase

**Date** : 30 -Nov- 2025

---

## 1. Introduction
Quantumcomputing introduced a new compuatational paradigm bulid upon the principles quantum mechanic . Unlike classical bit ,which take value 0 and 1 quantum qubit can exist
Superposition and form entabngles state.
entanglement is one of the mos non - classical phenomana - is crucial for quantum speed-ups ans quantum communication.
This mini project Demonstrate:
- Construction of Quantum State circuit
- Preparation of Bell state
- Verification of quntum entanglement through correlated measurement.
- Execution using Qiskit Quantum computoing Framework.
  
This project is serve as foundational exercise for begginers learning qunatum circuit and measurement bahaviour.

---
## 2. Objective
The goals of this project are:
1. Build q 2-Qubit state quantum circuit
2. create superposition and entangled state
3. simulate measurement outcome
4. show the meadurement result are perfectly correlated ,thereby proving entanglement.

---
## 3. Background Theory
### 3.1. Qubits and superposition


A **qubit** is a quantum bit that can exist in a superposition of both $|0\rangle$ and $|1\rangle$ states simultaneously.

#### General Qubit Representation

The general state of a single qubit, $|\psi\rangle$ (psi), is described using the following equation:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

The coefficients $\alpha$ and $\beta$ determine the probability of measuring the qubit in either state. The sum of the squares of their magnitudes must equal one:

$$|\alpha|^2 + |\beta|^2 = 1$$

#### Creating Superposition

A common operation to create an equal superposition is applying the Hadamard gate (H gate), which results in the $|+\rangle$ state:

$$|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$

#### Example -Hadamard Gate(H-Gate)

The **Hadamard (H) gate** is a crucial single-qubit gate used to create superposition.

It transforms the computational basis states $|0\rangle$ and $|1\rangle$ into even superpositions:

*   **Starting in $|0\rangle$:**
    $$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} = |+\rangle$$

*   **Starting in $|1\rangle$:**
    $$H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}} = |-\rangle$$

---

### 3.2.Entanglement

Quantum entanglement is a phenomenon where two or more quantum particles become linked in such a way that their fates are intertwined, regardless of the distance separating them. When measured, their individual quantum states remain correlated.

Entanglement occurs when particles interact and subsequently cannot be described independently of each other. The combined system has a single, unified quantum state.

Key points:

*   **Non-Locality**: A measurement performed on one particle instantly influences the state of the other(s),seeming to violate the speed of light—a concept famously dubbed "spooky action at a distance" by Albert Einstein.
*   **Correlation**: If you measure the spin (or polarization) of one entangled particle to be "up", you instantly know the spin of the other must be "down" (or vice versa), depending on how they were prepared.



## 3.3 Bell States (EPR Pairs)

Bell states, named after physicist John Stewart Bell, are a set of four specific, maximally entangled two-qubit (two-quantum bit) states. 
They form an orthonormal basis for a two-qubit system. These states are also often referred to as EPR (Einstein-Podolsky-Rosen) pairs.

The four standard Bell states are represented using the Dirac notation ($\vert \cdot \rangle$) and the tensor product ($\otimes$, often implied):

| NameState | Equation | Description |
| Phi Plus\ | (|\Phi ^{+}\rangle =\frac{1}{\sqrt{2}}(|00\rangle +|11\rangle )\) | Both qubits are the same (either both 0 or both 1). |
| Phi Minus\ | (|\Phi ^{-}\rangle =\frac{1}{\sqrt{2}}(|00\rangle -|11\rangle )\) |Both qubits are the same, with a relative phase shift. |
| Psi Plus\ | (|\Psi ^{+}\rangle =\frac{1}{\sqrt{2}}(|01\rangle +|10\rangle )\) |Qubits are different (one 0, one 1). |
| Psi Minus\ | (|\Psi ^{-}\rangle =\frac{1}{\sqrt{2}}(|01\rangle -|10\rangle )\) |Qubits are different, with a relative phase shift. |

---

## 4. Methodology
###Tools used-
**Programming language** : Python
**Quantum Framework** : Qiskit
**Simulator** : AerSimulator()
**plotting** : Matplotlib

----

## 5.Algorithm:
1.Installed and import Qiskit
2. Created 2-Qubit Quantum circuit 
3. Applied hadadamrd gate to qubit 0
4. Applied CNOT gate on qubit 0 to 1.
5. Measure Both Qubits
6. run on simulator with 1024 shots
7. produces analyze histrogram result.

---
## 5.Circuit Diagram
<img width="369" height="238" alt="image" src="https://github.com/user-attachments/assets/6448a784-ea87-4af2-9662-54ef05b4f7f3" />

---
## 6. Measurement Output
<img width="390" height="390" alt="image" src="https://github.com/user-attachments/assets/075872f6-415d-4653-ba15-e6b0f8236d54" />

#### 6.3 Proof of Entanglement
the perfect correlation is the indicator of entanglement :
P(00) =P(11) ==0.5, P(01)=P(10)==0
This match expected probability distribution of state $ {\|phi^+>| $
Thus Qunatum  state successfully demonstarte **Quantum Entanglement**

---

## 7. Discussion
- The project showcases one of the simplest yet most powerful aspect of qunatum mechanics.
-  The entangling operation via CNOT create not-classical correlation.
-  Even though measurement are physiccaly seperate ,measurement one of the instanteneously determine state of other.
-  This Project lays the foundation for future topic such as:
   - Quantum Teleporation
   - Superdence coding
   - Quantum Key Distribution
   - Multi Qubit Algorithm

---

## 8. Conclusion 
This Mini-Project successfully acheived its objective:
- A quantum circuit was constructed
- A Bell state was created
- simulation produced correlated measurement
- Entanglement was verified

---

## 9.Reference
- Qiskit Documentation(https://qiskit.org/documentation)
- Nielsen & chuang,Quantum Computation and Quantum Information
__







