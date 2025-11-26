# Day3 Notes - Linear Algebra For Quantum computing

Linear Algebra is the mathematical foundation of quantum computing.
Quantum States ,gates and measurements are all express using vectors and matrices.

---

## 1.Qubits As vectors
A Qubit is a 2-diamensional complex vector.Qubit is the basic unit of quantum information representation which help to describe quantum state in system.
|0> =[1,0]T
|1> =[0,1]T
A General qubits:
|Ψ> =α|0> + β|1>

|α><sup>2</sup> + |β><sup>2</sup> = 1

---

## 2. Bras and Kets(Dirac Notation)
- **Ket** - represent Column vector --> |Ψ>
- **Bra** - represent Row Vector i.e complex conjugate of column vector --> <Ψ|

---
  
## 3.inner pruduct (<Ψ|Φ>)
Inner product is core concept in quantum mechanic.It measures the **overlap** or **similarity** between two quantum states.
for two quantum state |Ψ> and |Φ> inner product = <Ψ|Φ>. this means probability amplitude transition from state |Ψ> to |Φ>.
- if inner product two same state <1|1> = <0|0> = 1 represeent state is Normalized.
- if inner product two different state <0|1> = <1|0> = 0 represeent state is Orthogonal.
  Hence all state in quantum system required Orthonormal to perform operation.

---

## 4. Norm of Quantum State 
Normalization ensure total probability into 1.all quantum state are normalized.
it represent valied quantum state.
normalization represent inner product of two same state must be 1.

|| |Ψ> || = 1 or <Ψ|Ψ> = 1.

---

## 5.Superposition
Quantum Superposition refer Qubits can be exist in multiple state at the same time until its measurement.i.e Qubit in state **|0> and |1>** simulteneously.
Example:

|+> = (|0> + |1>)/<sqrt>2</sqrt>

|-> = (|0> - |1>)/<sqrt>2</sqrt>

---

## 6.Tensor Product(⊗)
Tensor product used combine vector or matrices into larger Dimension. in quantum computing Tensor product is used to represent multi-qubit system.
|0> ⊗ |1> = |01> = [0,1,0,0]^T
Tensor size doubles with each qubit - 2<sup>n</sup> dimensional.

---

## 7. Quantum Gate as Matrices
Quantum gates must be matrices, this matrices are specially called "Unitary matrices" .unitary matrix is the square matrix whose complex conjugate transpose is also its inverse.
mathematically, U<sup>+</sup>U = UU<sup>+<\sup> = I(Identity matrix).
this means U and U<sup> + </sup>bring back you in original state,it help to prevent norm.
we apply Uniatry operation on state |Ψ> represented as: |Ψ<sup> , </sup>> = U|Ψ>.

---

## 8.Eigenvalues and Eigenvectors  
Eigenvalues and Eigenvectors are useful for quantum phase estimation.eigenvalue are +1 or -1 and eigenvectors are |0> or |1>.
If , U|v> = λ|V>

where,
|v> is Eigenvector and λ is the scaler EigenValue.

---

## 9.Why linear algebra matters in quantum computation
- state Evolution - matrix multiplication
- Multi-Qubit system - tensor product
- Measurement related to vector norms
- Quantum algorithm relay on eigenstructure
- unitary ensures probability  is preserved

  ---

  ## Summery
  By mastering linear algebra , you unlocked the mathematical model of quantum computing and implement real quantum algorithm in qiskit,cirq etc.this is  personalize study notes
  for understanding each concepts.

---

**written By** : Shreya Palase

**Date** - 26-Nov-2025**

Keep study,keep practice!
Thank you.
