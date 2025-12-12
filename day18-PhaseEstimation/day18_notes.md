# Day18 Notes- Quantum Phase Estimation (QPE) 

## 1. Introduction to Quantum Phase Estimation

Quantum Phase Estimation (QPE) is a foundational quantum algorithm used in Shor’s factoring algorithm, quantum chemistry, Hamiltonian eigenvalue estimation, and amplitude estimation.

QPE estimates an unknown phase φ for an eigenvalue of a unitary operator.  
If a unitary operator U has an eigenvector |ψ⟩ such that:

$$
U|\psi\rangle = e^{2\pi i \phi}|\psi\rangle,\quad 0 \le \phi < 1
$$

the goal is to estimate φ with high precision.

---

## 2. Why Phase Estimation Is Fundamental?

Many quantum algorithms rely on finding eigenvalues of a unitary operator:

- Shor’s algorithm (order finding)  
- Quantum chemistry (Hamiltonian eigenvalues)  
- Amplitude estimation (quadratic speedup)

QPE extracts eigenvalues by encoding a phase into amplitudes using controlled powers of U and decoding it via the inverse QFT.

---

## 3. Mathematical Setting of QPE

Given:

- A unitary operator U  
- An eigenstate |ψ⟩ satisfying

$$
U|\psi\rangle = e^{2\pi i \phi}|\psi\rangle
$$

We want to estimate φ with **n bits of precision**.

### Register Structure

- First register: n qubits, stores the binary estimate of φ  
- Second register: eigenstate |ψ⟩  

Initial state:

$$
|0\rangle^{\otimes n} \otimes |\psi\rangle
$$

After Hadamard gates on the first register:

$$
\frac{1}{2^{n/2}} \sum_{k=0}^{2^n-1} |k\rangle \otimes |\psi\rangle
$$

---

## 4. Controlled Unitaries and Phase Encoding

Each qubit in the first register controls a power of U:

- j-th qubit applies \( U^{2^j} \)

For basis state |k⟩:

$$
|k\rangle |\psi\rangle \rightarrow |k\rangle U^{k}|\psi\rangle = |k\rangle e^{2\pi i k\phi} |\psi\rangle
$$

Thus, phase information is encoded:

$$
\frac{1}{2^{n/2}} \sum_{k=0}^{2^n -1} e^{2\pi i k\phi} |k\rangle \otimes |\psi\rangle
$$

The second register is no longer needed; all phase info sits in the first.

---

## 5. Why the Inverse QFT Extracts the Phase

Before inverse QFT, the first register is:

$$
\frac{1}{2^{n/2}} \sum_{k=0}^{2^n -1} e^{2\pi i k\phi} |k\rangle
$$

Let φ have binary expansion:

$$
\phi = 0.\phi_1\phi_2 \ldots \phi_n
$$

Let:

$$
m = \phi \cdot 2^n,\qquad N = 2^n
$$

Then:

$$
e^{2\pi i k\phi} = \omega_N^{km},\qquad \omega_N = e^{2\pi i/N}
$$

The inverse QFT yields:

$$
\frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \omega_N^{km}|k\rangle \rightarrow |m\rangle
$$

This corresponds to the binary digits:

$$
|m\rangle = |\phi_1\phi_2\ldots\phi_n\rangle
$$

---

## 6. QPE for a Single-Qubit Rotation

Consider:

$$
U = R_z(\theta)
$$

Eigenvalues:

$$
U|1\rangle = e^{i\theta}|1\rangle,\qquad U|0\rangle = |0\rangle
$$

Thus:

$$
e^{i\theta} = e^{2\pi i\phi}
$$

So:

$$
\phi = \frac{\theta}{2\pi}
$$

### Controlled Powers of U

Controlled application:

$$
U^{2^j} = R_z(2^j\theta)
$$

Each contributes phase:

$$
\frac{2^j\theta}{2\pi} = 2^j\phi
$$

Phase is encoded exponentially.

---

## 7. Full Mathematical Derivation of QPE

### Step 1: Initialize

$$
|\Psi_0\rangle = |0\rangle^{\otimes n} |\psi\rangle
$$

### Step 2: Apply Hadamards

$$
|\Psi_1\rangle = \frac{1}{2^{n/2}} \sum_{k=0}^{2^n -1} |k\rangle |\psi\rangle
$$

### Step 3: Apply Controlled-\(U^{2^j}\)

Using:

$$
U^{k}|\psi\rangle = e^{2\pi i k\phi}|\psi\rangle
$$

State becomes:

$$
|\Psi_2\rangle = \frac{1}{2^{n/2}}\sum_{k=0}^{2^n-1} e^{2\pi i k\phi} |k\rangle |\psi\rangle
$$

### Step 4: Apply Inverse QFT

Extracts phase:

$$
|\Psi_3\rangle = |\phi_1\phi_2\ldots\phi_n\rangle |\psi\rangle
$$

### Step 5: Measurement

Measuring the first register gives φ.

---


## Summary

- QPE estimates the phase ϕ from eigenvalues of the form:

$$
e^{2\pi i \phi}
$$

- Controlled powers of the unitary operator  U  encode the phase ϕ into the amplitudes of the computational basis states.

- The inverse Quantum Fourier Transform (inverse QFT) extracts this encoded phase and converts it into its binary representation.

- QPE underlies major quantum algorithms such as Shor’s algorithm, amplitude estimation, and quantum chemistry eigenvalue solvers.

- For a single-qubit rotation Rz​(θ), the corresponding phase is:

$$
\phi = \frac{\theta}{2\pi}
$$

---

**Written By** : Shreya Palase

**Date** : 11-Dec-2025

Thank you and Keep learning!
