# Day8 - Multi-Qubit System in Qunatum computing part1(2-Qubit Syatem)

This file provides a detailed overview of common 2-qubit quantum gates and their corresponding $4 \times 4$ matrix representations, which describe how the gates operate on the 4-dimensional state space of two qubits.

The standard basis ordering used for these $4 \times 4$ matrices is: $|00\rangle, |01\rangle, |10\rangle, |11\rangle$.

---

### Table of Contents   
1.  [CNOT Gate (Controlled-NOT)](#1-cnot-gate-controlled-not)
2.  [SWAP / iSWAP Gate](#2-swap--iswap-gate)
3.  [CZ Gate (Controlled-Z)](#3-cz-gate-controlled-z)
4.  [Controlled Rotations (CRX, CRY, CRZ)](#4-controlled-rotations-crx-cry-crz)
5.  [Controlled H-Gate (CH Gate)](#5-controlled-h-gate-ch-gate)
6.  [Controlled Phase Gate (CP Gate)](#6-controlled-phase-gate-cp-gate)
7.  [Custom Unitary 2-Qubit Unitary Gate](#7-custom-unitary-2-qubit-unitary-gate)

---

### 1. CNOT Gate (Controlled-NOT)

The CNOT gate acts on a control qubit and a target qubit. It flips the target qubit if the control is $|1\rangle$.
CNOT gate matrix:
$$
U_{\text{CNOT}} = \begin{pmatrix} 
1 & 0 & 0 & 0 \\ 
0 & 1 & 0 & 0 \\ 
0 & 0 & 0 & 1 \\ 
0 & 0 & 1 & 0 
\end{pmatrix}
$$

Inline Block (Within a 

---

### 2. SWAP / iSWAP Gate
SWAP Gate The SWAP gate exchanges the states of two qubits:
  $|a\rangle |b\rangle \rightarrow |b\rangle |a\rangle \ $
 | Name | Matrix Representation |
 |------| -----------------------|
 | SWAP | $ U_{\text{SWAP}}=\left(\begin{matrix}1&0&0&0\\ 0&0&1&0\\ 0&1&0&0\\ 0&0&0&1\end{matrix}\right)\ $ |

 ---

 ### iSWAP Gate
 The iSWAP gate swaps the amplitudes of the  $ |01\rangle \ and \|10\rangle \ $ states and applies a relative phase of $ i\ $.
 | Name | Matrix Representation |
 |------| -----------------------|
 | iSWAP |$ U_{\text{iSWAP}}=\left(\begin{matrix}1&0&0&0\\ 0&0&i&0\\ 0&i&0&0\\ 0&0&0&1\end{matrix}\right)\ $ |

 ---

 ### 3. CZ Gate (Controlled-Z)
 The CZ gate applies a phase flip to the second qubit if the first qubit is $ |1\rangle \ $.
 The control and target qubits are interchangeable for this gate.
  | Name | Matrix Representation |
  |------| -----------------------|
  |CZ | $ U_{\text{CZ}}=\left(\begin{matrix}1&0&0&0\\ 0&1&0&0\\ 0&0&1&0\\ 0&0&0&-1\end{matrix}\right)\ $ |

  ---

  ### 4. Controlled Rotations (CRX, CRY, CRZ)
These gates apply a standard single-qubit rotation gate (RX, RY, or RZ) to the target qubit, conditioned on the control qubit being in the $ |1\rangle\ $ state.Let $ R_{k}(\theta )\ $ be the single-qubit rotation matrix around axis $ k\ $ by angle $ \theta \ $. The general structure of a controlled gate acting on the second qubit (using Qiskit ordering convention) is a block-diagonal matrix: $ U_{\text{Controlled-R}}=\left(\begin{matrix}I_{2\times 2}&0\\ 0&R_{k}(\theta )\end{matrix}\right)\ $
  Gate Description
  - CRX(\(\theta \))Controlled X-rotation.
  - CRY(\(\theta \))Controlled Y-rotation.
  - CRZ(\(\theta \))Controlled Z-rotation.

  ---

  ### 5. Controlled H-Gate (CH Gate)
  The CH gate applies the Hadamard gate (H) to the target qubit only when the control qubit is $ |1\rangle \ $.The Hadamard matrix is $  H=\frac{1}{\sqrt{2}}\left(\begin{matrix}1&1\\ 1&-1\end{matrix}\right)\ $
  | Name | Matrix Representation |
  |------| -----------------------|
 | CH |$ U_{\text{CH}}=\left(\begin{matrix}1&0&0&0\\ 0&1&0&0\\ 0&0&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\ 0&0&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{matrix}\right)\ $ |
  
  ---

  ### 6. Controlled Phase Gate (CP Gate)
  The CP gate (also known as cu1) introduces a relative phase $ e^{i\phi }\ $ to the state $ |11\rangle\ $.
  | Name | Matrix Representation |
  |------| -----------------------|
  | CP | $ {\phi }\\(U_{\text{CP}}=\left(\begin{matrix}1&0&0&0\\ 0&1&0&0\\ 0&0&1&0\\ 0&0&0&e^{i\phi }\end{matrix}\right))\ $ |

  ---

  ### 7. Custom Unitary 2-Qubit Unitary Gate
  This concept represents the ability to apply any valid $ 4\times 4\ $ complex unitary matrix ($ U\ $) that acts on the 4-dimensional two-qubit Hilbert space.
  | Name | Matrix Representation |
  |------| -----------------------|
  | Custom U |$ U_{\text{Custom}}=\left(\begin{matrix}U_{00}&U_{01}&U_{02}&U_{03}\\ U_{10}&U_{11}&U_{12}&U_{13}\\ U_{20}&U_{21}&U_{22}&U_{23}\\ U_{30}&U_{31}&U_{32}&U_{33}\end{matrix}\right)\ $
  Requirement: The matrix $ U\ $ must satisfy the condition of unitarity: $ U^{\dag }U=I\ $, where $ {\dag }\ $ is the conjugate transpose and $ I\ $ is the identity matrix.

---
**Written By** : Shreya Palase

**Date**: 1-Dec-2025

Thank you and Keep Learning!




