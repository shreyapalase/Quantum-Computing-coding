# Day8 - Multi-Qubit System in Qunatum computing part2(3-Qubit Syatem)

This file provides a detailed overview of common 3-qubit quantum gates and their corresponding $4\times 4$ matrix representations, which describe how the gates operate on the 4-dimensional state space of two qubits.

The standard basis ordering used for these $4\times 4$ matrices is: $|00\rangle, |01\rangle, |10\rangle, |11\rangle$.

---

### Table of Contents   
1.  [CCX Gate (Controlled-CNOT)](#1-controlled-cnot)
2.  [CSWAP Gate](#2-controlled-swap-gate)
3.  [CCZ Gate (Controlled-CZ)](#3-cz-gate-controlled-z)
4.  [Multi Controlled Rotations (MCRX, MCRY, MCRZ)](#4-multi-controlled-rotations-crx-cry-crz)
5.  [Multi Controlled Phase Gate (CP Gate)](#6-multi-controlled-phase-gate-cp-gate)
6.  [Custom Unitary 3-Qubit Unitary Gate](#7-custom-unitary-3-qubit-unitary-gate)

---
## CCX Gate (Controlled-CNOT / Toffoli Gate)

The **CCX gate**, also known as the **Toffoli gate**, is a three-qubit reversible quantum gate.  
It contains **two control qubits** and **one target qubit**.

### - Key Properties
- Performs a NOT operation on the target qubit **only when both control qubits are in the state** `|1⟩`.
- Represents a fundamental building block of **reversible classical logic**.
- Can be used to construct complex circuits such as **adders, comparators, and arithmetic units**.
- Fully preserves superposition and entanglement, enabling conditional quantum operations.
- Equivalent to applying a **CNOT** on the target, conditioned on two controls simultaneously.

### - Theoretical Description
The gate action can be summarized as:
- If the control qubits are **not both 1**, the target qubit is unchanged.
- If the control qubits are **both 1**, the target qubit is flipped:
  - `|110⟩ → |111⟩`
  - `|111⟩ → |110⟩`

### - Matrix Form
The CCX gate is represented by the following 8×8 unitary matrix (in computational basis):

$$
\begin{bmatrix}
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1\\
0&0&0&0&0&0&1&0
\end{bmatrix}
$$

### - Applications
- Building universal classical logic circuits on quantum computers.
- Creating multi-controlled quantum operations.
- Used in algorithms requiring conditional logic, such as:
  - Arithmetic circuits  
  - Quantum ripple-carry adders  
  - Reversible computing systems  


​----

## CSWAP Gate (Controlled-SWAP / Fredkin Gate)

The **CSWAP gate**, also known as the **Fredkin gate**, is a three-qubit reversible quantum gate.  
It consists of **one control qubit** and **two target qubits**.

### Key Properties
- Swaps the states of the two target qubits **only when the control qubit is in the state** `|1⟩`.
- If the control qubit is `|0⟩`, the target qubits remain unchanged.
- It is an important gate for **reversible computation** and **quantum comparison and sorting tasks**.
- Preserves superposition and entanglement between the swapped qubits.

### Theoretical Description
The action of the CSWAP gate:
- If the control qubit is `0`:
  - `|0ab⟩ → |0ab⟩` (no swap)
- If the control qubit is `1`:
  - `|1ab⟩ → |1ba⟩` (swap targets)

### Matrix Form
The CSWAP gate is represented by the following 8×8 unitary matrix:

\[
\begin{bmatrix}
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1
\end{bmatrix}
\]

### Applications
- Quantum **comparison**, **routing**, and **sorting networks**.
- Useful in **quantum machine learning** models involving data comparison.
- Serves as a fundamental component in **reversible logic circuits**.
- Applies a conditional swap while fully preserving quantum coherence.


---

## CCZ Gate (Controlled-Controlled-Z Gate)

The **CCZ gate** is a three-qubit controlled phase gate with **two control qubits** and **one target qubit**.  
It applies a Z-phase (a phase flip of `-1`) **only when all three qubits are in the state** `|111⟩`.

### Key Properties
- Applies a phase shift of `-1` to the basis state `|111⟩`.
- Leaves all other computational basis states unchanged.
- It is a **diagonal gate**, meaning it does not alter amplitude magnitudes—only relative phases.
- Can be converted into a **Toffoli (CCX) gate** by surrounding the target with Hadamard gates.
- Widely used in constructing multi-controlled quantum gates and phase-sensitive algorithms.

### Theoretical Description
The CCZ operation can be described as:
- For any state `|abc⟩`:
  - If `a = b = c = 1`, apply a phase flip: `|111⟩ → -|111⟩`
  - Otherwise: `|abc⟩` remains unchanged

### Matrix Form
The CCZ gate is represented by the following diagonal 8×8 unitary matrix:

\[
CCZ = \text{diag}(1, 1, 1, 1, 1, 1, 1, -1)
\]

### Applications
- Used in **phase kickback** and **interference-based algorithms**.
- Key component in **quantum Boolean logic** and multi-controlled circuit constructions.
- Appears frequently in algorithm

---


## Multi-Controlled Rotations (MCRX, MCRY, MCRZ)

Multi-Controlled Rotation gates extend single-qubit rotation operations (RX, RY, RZ) by adding **multiple control qubits**.  
The rotation is applied to the target qubit **only when all control qubits are in the state** `|1⟩`.

These gates enable precise, conditional manipulation of quantum amplitudes in multi-qubit systems.

---

### Key Properties
- Generalization of controlled rotation gates to **two or more control qubits**.
- Apply rotations around:
  - **X-axis:** MCRX(θ)  
  - **Y-axis:** MCRY(θ)  
  - **Z-axis:** MCRZ(θ)  
- Act only when *all* control qubits satisfy the condition `|1⟩`.
- Frequently used in **variational algorithms**, **quantum machine learning**, and **amplitude encoding circuits**.
- Provide fine-grained control over quantum states through adjustable rotation angles.

---

### Theoretical Description
For a rotation gate \( R_\alpha(\theta) \) (where_

5. Multi-Controlled Phase Gate (CP Gate)

## Multi-Controlled Phase Gate (CP Gate)

The **Multi-Controlled Phase (CP) gate** is a generalized controlled-phase operation that applies a phase shift  
\[
e^{i\theta}
\]
to a target qubit **only when all control qubits are in the state** `|1⟩`.

It extends the standard 2-qubit controlled-phase gate to systems with multiple controls, allowing precise, conditional manipulation of quantum phases.

---

### Key Properties
- Applies a phase factor \( e^{i\theta} \) to a target qubit or specific multi-qubit state.
- All computational basis states remain unchanged **except** the one where *all control qubits* are `|1⟩`.
- A diagonal gate (does not change amplitudes—only phases).
- Special cases:
  - When \( \theta = \pi \), it becomes a **multi-controlled Z (MCZ)** gate.
  - With two controls and \( \theta = \pi \), it becomes the **CCZ gate**.
- Fundamentally important for **phase kickback**, **interference**, and **quantum Fourier transform**.

---

### Theoretical Description
For a system with `n` control qubits and one target qubit:

- If not all control qubits are `1`, the state is unchanged.
- If all control qubits are `1`, the state picks up a phase:
  \[
  |11\ldots1\,\psi\rangle \rightarrow e^{i\theta} |11\ldots1\,\psi\rangle
  \]

The gate’s action is purely phase-based and does not affect probability amplitudes.

---

### Matrix Form (Generalized)
The multi-controlled phase gate has a diagonal matrix representation:

\[
\text{diag}(1, 1, \ldots, 1, e^{i\theta})
\]

The final diagonal element corresponds to the basis state where all control qubits are `1`.

---

### Applications
- Central to **quantum phase estimation** and **quantum Fourier transform (QFT)**.
- Used in **oracles for Grover’s algorithm**.
- Important for **state preparation**, **amplitude amplification**, and **multi-qubit interference patterns**.
- Enables flexible control of phase relationships in deeply entangled quantum systems.



----

## Custom 3-Qubit Unitary Gate

A **custom 3-qubit unitary gate** represents the most general quantum operation that can be applied to a system of three qubits.  
It is defined by an **8×8 unitary matrix**, where every transformation is reversible and preserves quantum coherence.

---

### Key Properties
- Acts on three qubits simultaneously using a single **8×8 complex unitary matrix**.
- Must satisfy the unitarity condition:
  \[
  U^\dagger U = I
  \]
  ensuring reversibility and valid quantum evolution.
- Represents the most expressive form of a three-qubit gate—capable of performing any physically allowed transformation.
- Can encode any multi-qubit logic, entangling operation, or custom-designed quantum behavior.

---

### Theoretical Description
A custom unitary operation on three qubits transforms a basis state \( |x\rangle \) (where \( x \in \{0,1\}^3 \)) into a superposition:

\[
|x\rangle \rightarrow U |x\rangle
\]

Because the matrix is unitary, it:
- Preserves inner products  
- Maintains normalization  
- Ensures reversibility  

These properties make it possible to create arbitrarily complex quantum operations.

---

### Matrix Form
The gate is fully described by:

\[
U \in \mathbb{C}^{8 \times 8}, \quad U^\dagger U = I
\]

The matrix may include rotation, phase, mixing, and entangling components all at once.

---

### Applications
- Designing custom logic in quantum algorithms.
- Creating specialized **entangling operations** not available in standard gate libraries.
- Implementing **problem-specific oracles**, **state preparation routines**, and **Hamiltonian simulations**.
- Prototyping experimental quantum hardware behaviors.
- Useful in variational circuits where **trainable unitary blocks** are required.

---
## Custom 3-Qubit Unitary Gate (Summary)

A custom 3-qubit unitary gate is an arbitrary **8×8 unitary matrix** acting on three qubits.  
It performs any reversible quantum operation while preserving normalization and coherence.  
Used for implementing specialized transformations, custom logic, entangling operations, and problem-specific quantum algorithms.
---

**Written By** : Shreya Palase

**Date** : 2-Dec-2025

Thank you and keep learning!
