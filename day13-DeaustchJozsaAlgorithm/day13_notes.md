# Day13 Notes- Deutsch–Jozsa Algorithm

## 1. Introduction

The Deutsch–Jozsa algorithm is one of the first algorithms to show exponential advantage of quantum computing over classical deterministic computation.  
It determines whether a Boolean function is constant or balanced with a single oracle call.

---

## 2. Problem Definition

We are given a function

$$
f: 0,1^n \longrightarrow 0,1
$$

The function is promised to be either:

### Constant

$$
f(x) = c \quad c \in 0,1
$$

### Balanced

The output is zero for half the inputs and one for the other half.

### Goal

Determine whether the function is constant or balanced.

---

## 3. Quantum Oracle

The oracle is a unitary gate defined as

$$
U_f \mid x,y \rangle = \mid x,\, y \oplus f(x) \rangle
$$

where ⊕ is XOR.

---

## 4. Algorithm Outline

1. Initialize qubits  
2. Apply Hadamard gates  
3. Apply the oracle  
4. Apply Hadamard gates again  
5. Measure the first n qubits

---

## 5. Detailed Working

### 5.1 Initialization

We start with n qubits in state mid 0 rangle and one auxiliary qubit in mid 1 rangle.

Initial state:

$$
\mid \psi_0 \rangle = \mid 0^n \rangle \mid 1 \rangle
$$

---

### 5.2 Apply Hadamard Gates

Applying Hadamard to all input qubits:

$$
H^{\otimes n} \mid 0^n \rangle = \frac{1}{\sqrt{2^n}} \sum_x \mid x \rangle
$$

Auxiliary qubit transform:

$$
H \mid 1 \rangle = \frac{\mid 0 \rangle - \mid 1 \rangle}{\sqrt{2}}
$$

Total state becomes:

$$
\mid \psi_1 \rangle =
\frac{1}{\sqrt{2^{n+1}}}
\sum_x \mid x \rangle (\mid 0 \rangle - \mid 1 \rangle)
$$

---

### 5.3 Oracle Application

Oracle action:

$$
U_f \mid x \rangle (\mid 0 \rangle - \mid 1 \rangle)
= \mid x \rangle (\mid f(x) \rangle - \mid 1 \oplus f(x) \rangle)
$$

Using XOR properties:

$$
\mid f(x) \rangle - \mid 1 \oplus f(x) \rangle
= (-1)^{f(x)}(\mid 0 \rangle - \mid 1 \rangle)
$$

Thus:

$$
\mid \psi_2 \rangle =
\frac{1}{\sqrt{2^{n+1}}}
\sum_x (-1)^{f(x)} \mid x \rangle (\mid 0 \rangle - \mid 1 \rangle)
$$

The auxiliary qubit factors out.

---

### 5.4 Apply Final Hadamard Transform

Hadamard identity:

$$
H^{\otimes n} \mid x \rangle =
\frac{1}{\sqrt{2^n}}
\sum_z (-1)^{x \cdot z} \mid z \rangle
$$

Full state becomes:

$$
\mid \psi_3 \rangle =
\frac{1}{2^n}
\sum_z
\left(
\sum_x (-1)^{f(x)} (-1)^{x \cdot z}
\right)
\mid z \rangle
(\mid 0 \rangle - \mid 1 \rangle)
$$

Amplitude of the zero state:

$$
A_0 = \frac{1}{2^n} \sum_x (-1)^{f(x)}
$$

---

## 6. Interpretation

### Case 1: Function is constant

If f outputs zero for all x:

$$
(-1)^{f(x)} = 1
$$

Sum becomes:

$$
\sum_x 1 = 2^n
$$

Thus:

$$
A_0 = 1
$$

If f outputs one for all x:

$$
(-1)^{f(x)} = -1
$$

Sum:

$$
\sum_x (-1) = -2^n
$$

Amplitude magnitude is still 1.

Measurement always produces:

$$
\mid 0^n \rangle
$$

---

### Case 2: Function is balanced

Half the terms contribute plus one, half minus one:

$$
\sum_x (-1)^{f(x)} = 0
$$

Thus:

$$
A_0 = 0
$$

Meaning:

$$
\mid 0^n \rangle
$$

never appears as measurement output.

---

## 7. Decision Rule

- If the measurement result is the all zero state, the function is constant.  
- Otherwise, the function is balanced.

The algorithm uses **one** oracle query.

---

## 8. Quantum Advantage

### Classical deterministic complexity

$$
2^{n-1} + 1
$$

### Quantum complexity

$$
1
$$

This is an exponential quantum speedup.

---

## 9. Summary

The Deutsch–Jozsa algorithm shows how quantum superposition, phase kickback, and interference can extract global properties of a function with exponentially fewer queries than classical algorithms.

---

**Written By** : Shreya Palase

**Date** : 6-Dec-2025

Thank you and Keep Learning!
