# Day 17 Notes - Quantum Fourier Transform (QFT) 
In this notes, we describe what the Quantum Fourier Transform is, how it works mathematically, and how to build and validate a 3-qubit QFT and its inverse.

---

## 1. Formal Definition of the Quantum Fourier Transform

For an n-qubit system, the number of states is:

$$
N = 2^n
$$

The Quantum Fourier Transform is defined as:

$$
\text{QFT}\,|x\rangle=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i xk}{N}}|k\rangle
$$

---

## 2. Binary Expansion and Phase Encoding

Binary expansion of an integer x:

$$
x = x_0 2^0 + x_1 2^1 + \dots + x_{n-1}2^{n-1}
$$

Binary fraction identity:

$$
\frac{k}{2^n} = 0.k_1 k_2 \dots k_n
$$

Phase rewriting:

$$
e^{\frac{2\pi i xk}{2^n}}=e^{2\pi i x(0.k_1 k_2 \dots k_n)}
$$

---

## 3. How QFT Works Mechanically

Initial computational basis state:

$$
|x\rangle = |x_{n-1} x_{n-2} \dots x_0\rangle
$$

Factorized QFT output:

$$
\text{QFT}|x\rangle=\frac{1}{2^{n/2}}\bigotimes_{j=0}^{n-1}\left(|0\rangle +e^{2\pi i\,0.x_j x_{j-1}\dots x_0}|1\rangle\right)
$$

---

## 4. The QFT Process Step-by-Step

### Step 1 — Hadamard on the most significant qubit

$$
H|x_{n-1}\rangle=\frac{1}{\sqrt{2}}\left(|0\rangle +e^{2\pi i x_{n-1}/2}|1\rangle\right)
$$

### Step 2 — Controlled Phase Rotations

Controlled phase rotation matrix:

$$
R_k =\begin{pmatrix}1 & 0 \\0 & e^{2\pi i / 2^k}\end{pmatrix}
$$

Phase contribution added by lower-order qubits:

$$
e^{2\pi i\,0.x_{j-1}x_{j-2}\dots x_0}
$$


### Step 3 — Repeat for all qubits

Each qubit receives:
- One Hadamard  
- Controlled rotations with smaller-index qubits  

---

### Step 4 — Swap Operations

Bit order correction:

$$
|q_{n-1} \dots q_0\rangle\rightarrow|q_0 \dots q_{n-1}\rangle
$$

---

## 5. Inverse Quantum Fourier Transform

Definition of inverse QFT:

$$
\text{QFT}^{-1}|k\rangle=\frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}e^{-2\pi i xk / N}|x\rangle
$$

Verification:

$$
\text{QFT}^{-1}(\text{QFT}|x\rangle) = |x\rangle
$$

--- 

## 6. Example: 3-Qubit QFT

Number of states:

$$
N = 8
$$

Definition:

$$
\text{QFT}|x\rangle=\frac{1}{\sqrt{8}}\sum_{k=0}^{7}e^{2\pi i xk/8}|k\rangle
$$

Expanded output in binary:

$$
\frac{1}{\sqrt{8}}\left(|0\rangle + e^{2\pi i\,0.x_0}|1\rangle\right)\otimes\left(|0\rangle + e^{2\pi i\,0.x_1 x_0}|1\rangle\right)\otimes\left(|0\rangle + e^{2\pi i\,0.x_2 x_1 x_0}|1\rangle\right)
$$

---

## 7. What We Learned

- Mathematical intuition behind QFT  
- How binary fractions encode phase information  
- Gate-by-gate construction of QFT  
- Why swap gates are needed  
- Inverse QFT as reverse process  
- Complete 3-qubit QFT example  

---

**Written By** : Shreya Palase

**Date** : 10-Dec-2025

Thank you and keep learning!

