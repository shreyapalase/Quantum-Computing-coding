# Day 22 Notes - Variational Quantum Eigensolver (VQE) Algorithm

## Introduction
The **Variational Quantum Eigensolver (VQE)** is a hybrid quantum-classical algorithm used to solve quantum chemistry problems, particularly to determine the ground state energy of molecules. It combines the power of quantum computers for the preparation of quantum states with the flexibility of classical computers to optimize parameters of a quantum circuit. This makes it suitable for near-term quantum devices, which may not have enough qubits or error-correction mechanisms to implement purely quantum algorithms like **Quantum Phase Estimation (QPE)**.

In this , we will demonstrate how the **VQE algorithm** works using the example of the **H₂ molecule** and its ground state energy. The topics covered include the following:

- Why **Variational Quantum Eigensolver (VQE)** is used in quantum chemistry
- The main goal of the VQE algorithm
- How molecular Hamiltonians are solved using quantum circuits
- Parametrized ansatz and its role in VQE
- Expectation value calculation
- How to compute the ground state energy of the H₂ molecule

---

## 1. **Why VQE is Used in Quantum Chemistry**

In quantum chemistry, solving for the **ground state energy** of a molecule is crucial for understanding its properties, such as stability, reactivity, and interaction with other molecules. The classical methods often face limitations due to the exponential growth of the Hilbert space with increasing system size (number of electrons and orbitals). This problem becomes especially difficult for larger molecules, where **Hartree-Fock (HF)** or **Density Functional Theory (DFT)** methods may become inaccurate.

The **VQE algorithm** addresses this challenge by offering a quantum-classical approach to efficiently compute the ground state energy, using **quantum circuits** to represent quantum states and **classical optimization** to find the best parameters. The advantage of VQE lies in its potential to work on near-term quantum computers, making it practical for real-world applications even with current quantum technology.

---

## Pseudocode for VQE Implementation for H₂ Molecule
1. Initialize the quantum system for H₂ molecule
   - Define the qubits and quantum registers
   - Prepare the molecular Hamiltonian H (decomposed into Pauli matrices)
   
2. Prepare the parameterized ansatz circuit:
   - Choose an appropriate ansatz (e.g., Hardware-efficient, UCCSD)
   - Initialize parameters for the ansatz (e.g., random initial angles for rotations)

3. Classical Optimization Setup:
   - Define a classical optimizer (e.g., COBYLA, L-BFGS-B)
   - Set up the optimization loop and stop criteria (e.g., maximum iterations, convergence threshold)

4. Define the objective function (expectation value of the Hamiltonian):
   - For each set of parameters:
     - Apply the ansatz to prepare the quantum state
     - Calculate the expectation value of the Hamiltonian:
       - Measure the quantum state to get the outcome of the Pauli operator terms (e.g., II, IZ, ZZ)
       - Compute the weighted sum of the measured values using the coefficients of each Pauli term

5. Optimization Loop (Iterative Process):
   - For each iteration of the classical optimizer:
     - Evaluate the objective function by computing the expectation value of the Hamiltonian for the current parameters
     - Update the parameters of the ansatz using the classical optimizer to minimize the expectation value of H
     - Check convergence criteria (e.g., if the energy change between iterations is below a threshold)

6. Final Result:
   - The final set of optimized parameters corresponds to the quantum state that approximates the ground state
   - The optimized expectation value represents the ground state energy of the H₂ molecule

7. Output the ground state energy of H₂

---

## **The Main Goal of the VQE Algorithm**

The main goal of the **VQE algorithm** is to find the **ground state energy** of a quantum system, which is the lowest energy state of the system. This energy corresponds to the most stable configuration of the system (e.g., a molecule).

To achieve this, the VQE algorithm aims to:

1. Prepare a quantum state that approximates the ground state of the system.
2. Minimize the expectation value of the system's **Hamiltonian** $\hat{H}$ which represents the total energy of the system.
3. Use classical optimization techniques to adjust the parameters of the quantum circuit in order to minimize this expectation value.

In this notebook, we'll focus on the specific case of calculating the ground state energy of the **H₂ molecule** using VQE.

---

## 3. **How Molecular Hamiltonians Are Solved Using Quantum Circuits**

A **Hamiltonian** is a mathematical operator that represents the total energy of a quantum system, including the kinetic and potential energies. In the context of quantum chemistry, the molecular Hamiltonian describes the interactions between electrons and nuclei in a molecule.

For example, the **Hamiltonian for H₂** involves terms for the kinetic energy of the electrons, the Coulomb repulsion between electrons, and the attractive interaction between electrons and nuclei. These terms can be written as:

$$
\hat{H} = \hat{T}_e + \hat{V}_{ee} + \hat{V}_{ne}
$$

Where:
- $\hat{T}_e$ is the kinetic energy operator for the electrons.
- $\hat{V}_{ee}$ is the electron-electron repulsion term.
- $\hat{V}_{ne}$ is the electron-nucleus attraction term.

The Hamiltonian is typically expressed in terms of **Pauli matrices** (e.g., $\hat{X}, \hat{Y}, \hat{Z}$) in a **qubit basis**, which can be implemented on a quantum computer.

For example, a general Hamiltonian $\hat{H}$ can be decomposed as a sum of tensor products of Pauli matrices:

$$
\hat{H} = \sum_{i} c_i \hat{P}_i
$$

Where $\hat{P}_i$ are Pauli operators (e.g., $\hat{X}, \hat{Y}, \hat{Z}, \hat{I}$) and $c_i$ are real coefficients.

To solve the Hamiltonian using quantum circuits:
1. The Hamiltonian is **decomposed** into a sum of tensor products of Pauli matrices.
2. A **quantum circuit** is designed to prepare an approximate ground state.
3. The **expectation value** of the Hamiltonian is computed by measuring the quantum state.

---

## 4. **Parameterized Ansatz and its Role in VQE**

A **parameterized ansatz** is a trial quantum state that is used as an approximation to the true ground state of the system. In VQE, we represent the quantum state as a parameterized quantum circuit, where the parameters can be adjusted through classical optimization.

The ansatz is typically designed based on physical insights into the system. For example, the **Hartree-Fock state** or **UCCSD (Unitary Coupled Cluster Single and Double)** ansatzes are often used in quantum chemistry.

Let the quantum state at time $t be:

$$
|\psi(\theta)\rangle = U(\theta) |\psi_0\rangle
$$

Where:
- $U(\theta)$ is a unitary operator parameterized by $\theta$ (a set of classical variables).
- $|\psi_0\rangle$ is the initial state (e.g., Hartree-Fock state).

- The ansatz is implemented on a quantum computer, where **quantum gates** with adjustable parameters are applied to the qubits.
- The parameters of the ansatz are optimized using classical algorithms (e.g., gradient descent, Nelder-Mead, etc.) to minimize the expectation value of the Hamiltonian.

In the case of the H₂ molecule, the ansatz may involve a series of **single-qubit rotations** and **entangling gates** to capture the electron correlation.

---

## 5. **Expectation Value Calculation**

Once we have the quantum state prepared using the ansatz, the next step is to compute the expectation value of the Hamiltonian. This is done by measuring the quantum state in the computational basis and calculating the average outcome.

For a Hamiltonian $\hat{H}$, the expectation value $\langle \hat{H} \rangle$ is given by:

$$
\langle \hat{H} \rangle = \langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle
$$

Where $| \psi(\theta) \rangle$ is the parameterized quantum state and $\hat{H}$ is the Hamiltonian operator. This is done by repeatedly measuring the quantum state and calculating the average value of the operator's outcomes. Quantum computers can measure specific terms of the Hamiltonian by utilizing **Pauli measurements**.

In practice, the expectation value can be computed using the following relation:

$$
\langle \hat{P}_i \rangle = \frac{1}{N} \sum_{j=1}^{N} \langle \psi(\theta) | \hat{P}_i | \psi(\theta) \rangle_j
$$

Where $N$ is the number of shots (repeated measurements).

---

## 6. **How to Compute the Ground State Energy of the H₂ Molecule**

To compute the ground state energy of the **H₂ molecule**, the following steps are followed:

1. **Molecular Hamiltonian**: The Hamiltonian for the H₂ molecule is represented in terms of Pauli matrices. This requires the use of quantum chemistry software like **Qiskit** or **PySCF** to perform a **Hartree-Fock calculation**, which gives the starting point for the quantum simulation.

2. **Prepare the Ansatz**: We choose an ansatz (e.g., the **hardware-efficient ansatz**) that will allow us to approximate the ground state of the H₂ molecule. This ansatz is implemented as a quantum circuit with parameterized gates.

3. **Initialize Parameters**: The parameters of the ansatz are initialized with random values.

4. **Optimize Parameters**: Using a classical optimizer (such as **COBYLA** or **L-BFGS-B**), we minimize the expectation value of the Hamiltonian by adjusting the parameters of the quantum circuit.

5. **Measure the Expectation Value**: The quantum computer measures the expectation value of the Hamiltonian for each set of parameters, and the classical optimizer updates the parameters accordingly.

6. **Iterate Until Convergence**: This process continues iteratively until the ground state energy is found, i.e., the expectation value of the Hamiltonian converges to the minimum.

---

## 7. **Pauli Operators and Coefficients in the Hamiltonian**

In the decomposition of the Hamiltonian for quantum simulation, we often express the Hamiltonian in terms of **Pauli operators**. These operators include $I$ (identity),
$X$, $Y$, and $Z$ (the Pauli matrices). For the H₂ molecule, we represent the Hamiltonian as a sum of terms involving these Pauli matrices:

The Hamiltonian for the H₂ molecule can be written as:

$$
\hat{H} = c_{II} \hat{I} \otimes \hat{I} + c_{IZ} \hat{I} \otimes \hat{Z} + c_{ZI} \hat{Z} \otimes \hat{I} + c_{ZZ} \hat{Z} \otimes \hat{Z} + c_{XX} \hat{X} \otimes \hat{X}
$$

Where:
- #\hat{I}$ is the identity operator.
- $\hat{X}$, $\hat{Y}$, and $\hat{Z}$ are the Pauli matrices.
- $c_{II}, c_{IZ}, c_{ZI}, c_{ZZ}, c_{XX}$ are real coefficients determined by the molecular Hamiltonian.

### Purpose of Each Term:
- $\hat{I} \otimes \hat{I}$ represents a constant term in the Hamiltonian.
- $\hat{I} \otimes \hat{Z}$ and $\hat{Z} \otimes \hat{I}$ represent terms related to the interactions between the qubits in the quantum system, often describing electron-nucleus interactions.
- $\hat{Z} \otimes \hat{Z}$ represents terms involving electron-electron repulsion.
- $\hat{X} \otimes \hat{X}$ is part of the interaction terms, often related to exchange interactions or correlation effects.

These coefficients $c_{II}, c_{IZ}, c_{ZI}, c_{ZZ}, c_{XX}$ are computed from the **molecular integrals** of the Hamiltonian, and each Pauli term corresponds to a specific type of interaction between the qubits.

---

## Why Use COBYLA for Optimization in VQE?

The COBYLA (Constrained Optimization BY Linear Approximations) method is a popular choice for optimizing the parameters in the VQE algorithm due to the following reasons:

No Gradient Information Required: COBYLA is a derivative-free optimization method, meaning it does not require the gradient of the objective function (the expectation value of the Hamiltonian) to perform the optimization. This is particularly important for VQE because the quantum circuits are highly complex, and computing gradients may be difficult or computationally expensive.

Non-Linear Optimization: The optimization problem in VQE is typically non-linear, as the quantum state depends on parameters that interact in a highly non-linear fashion. COBYLA works well for such problems, providing a simple yet effective approach to finding the optimal parameters.

Handles Bound Constraints: VQE often requires constraints on the optimization parameters, such as bounds on the rotation angles of quantum gates. COBYLA efficiently handles these box constraints without requiring the user to explicitly calculate gradients.

Low-Dimensional Optimization: VQE typically involves optimizing a relatively small number of parameters (e.g., for small molecules like H₂). COBYLA is well-suited for this low-dimensional optimization, making it an efficient choice for small-scale quantum chemistry problems.

Well-Established: COBYLA is a well-tested method in the optimization community, and its reliability and robustness make it a good choice for variational quantum algorithms, where experimental noise and limited resources must be taken into account.

---

## Summary

The **VQE algorithm** is a powerful method for calculating the ground state energy of molecules using quantum computers. By leveraging parameterized ansatzes and classical optimization techniques, it can effectively handle complex quantum chemistry problems that are intractable for classical computers. In this notebook, we have explored how VQE can be applied to the **H₂ molecule**, covering key concepts such as the molecular Hamiltonian, parameterized ansatz, and expectation value calculation.

**Key Takeaways:**
- VQE is used in quantum chemistry to solve molecular energy problems.
- The main goal is to find the **ground state energy** of a molecule.
- **Quantum circuits** are used to represent quantum states, and **classical optimization** adjusts the parameters to minimize the energy.
- The Hamiltonian is decomposed into terms involving Pauli matrices, with specific coefficients for each interaction term.

This approach opens the door to solving larger, more complex molecular systems in the future, helping to unlock advances in materials science, pharmaceuticals, and chemical engineering.

---

**Written By** : Shreya Palase

**Date**: 16-Dec-2025

Thank you and Keep learning!
