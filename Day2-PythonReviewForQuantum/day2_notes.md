# Day2 - Python Review, Vectors and Matrices

## 1. Why vectors and matrices are matter in Quantum computing
Quantum computing is bulit on **Linear Algebra**
- a quantum state |Ψ> is a **vector**.
- a quantum gate (X,H,Z etc.) is a **2x2 matrix**
- State Evolution is computed using **matrix x vector**
  Understanding this fundamental for before moving toward for quantum computing

---
 ## 2. Python Essential review
 - variables
 - loops
 - functions
 - NumPy array for numerical computing
NumPy give efficient matrix math , which is required for simulating quantum system.

---
## 3. Vectors
Vector in qiantum computing is a complex valued column vector that describe the state of qubit or a system of qubit. it contains amplitude for each possible quantum state.
Examples:
- 2D vectors - represent qubit in computational basic.
- 3D vector - genearal linear algebra practice.
Operations:
- Addition - additing two vector
- Dot product -two vector sum of the product of their corrosponding component.

  ---
  ## 4.Matrix 2x2 and 3x3
  A Matrix in quantum computing is a complex valued ,square ,linear operators that acts on quantum state vectors to transform them according to the rule of quantum mechanic.
  it tell a qubit how to change. 
  example:
  Pauli-x matrix
  \[
  \begin{bmatrix}
  0 & 1 \\
  1 & 0
  \end{bmatrix}
  \]

  You practiced:
  - Addition - adding two matrices by summing their corresponding elements.
  - Multiplication-combine two matrices by summing the product of corresponding row and column element.
  - Determinant -it is scaler value that summerized certain properties of matrix such as whether it is invertible.
    

---
## 5.Matrix- Vector Multiplication
\[
|\psi'> = U|\psi>
\]
where:
- U is gate matrix
- |Ψ>  is a state vector

  Now you ready to deep dive into implementing linear algebra for quantum computing on next level.
  happy learning!
  ### Author : Shreya palase
  ### Date : 25-nov-2025
