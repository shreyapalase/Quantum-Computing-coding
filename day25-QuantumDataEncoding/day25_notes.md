# Day25 Notes - Quantum Data Encoding  
### Amplitude Encoding – From Classical Data to Quantum States  

---

## 1. Introduction to Quantum Data Encoding  

Quantum algorithms operate on **quantum states**, not classical numbers.  
To apply quantum computing to machine learning, optimization, or data analysis, **classical data must be encoded into quantum states**.  
This process is called **Quantum Data Encoding** (also known as quantum data embedding).

> **Goal:** Represent classical data using the amplitudes or properties of qubits so quantum algorithms can process it.

---

## 2. Why Quantum Data Encoding is Important  

Quantum computers provide advantages such as:
- Exponential state space growth
- Quantum parallelism
- Interference and entanglement

However, these advantages only matter **after data is loaded into quantum states**.

If data encoding is inefficient, quantum speedups may be lost.

---

## 3. Types of Quantum Data Encoding  

Common encoding strategies include:

| Encoding Type | Data Stored In | Notes |
|---------------|--------------|-------|
| Basis Encoding | Computational basis states | Simple but qubit-expensive |
| Angle Encoding | Rotation angles of gates | Hardware-efficient |
| **Amplitude Encoding** | Probability amplitudes | Exponentially compact |
| QSample Encoding | Measurement probabilities | Used in quantum ML |

In this notebook, we focus on **Amplitude Encoding**.

---

## 4. Concept of Amplitude Encoding  

### 4.1 Mathematical Idea  

A quantum state of $n$ qubits can represent $2^n$ complex amplitudes:

$$
|\psi\rangle = \sum_{i=0}^{2^n - 1} \alpha_i |i\rangle
$$

Where:
- $|i\rangle$ are computational basis states
- $\alpha_i \in \mathbb{C}$
- Normalization constraint:

$$
\sum_i |\alpha_i|^2 = 1
$$

---

### 4.2 Mapping Classical Data  

Given a classical vector:

$$
\vec{x} = (x_0, x_1, ..., x_{2^n-1})
$$

We encode it as:

$$
|\psi\rangle = \frac{1}{\|\vec{x}\|} \sum_{i=0}^{2^n-1} x_i |i\rangle
$$

Where:

$$
\|\vec{x}\| = \sqrt{\sum_i x_i^2}
$$

---

### 4.3 Key Advantages  

- Encodes $2^n$ values using only $n$ qubits
- Enables exponential compression
- Widely used in quantum machine learning

⚠️ **Tradeoff:** State preparation can be costly

---

## 5. Encoding a 4D Classical Vector Using 2 Qubits  

### 5.1 Classical Vector  

Let:

$$
\vec{x} = (x_0, x_1, x_2, x_3)
$$

This is a **4-dimensional vector**, so we need:

$$
2^n = 4 \Rightarrow n = 2 \text{ qubits}
$$

---

### 5.2 Normalization  

Compute the norm:

$$
\|\vec{x}\| = \sqrt{x_0^2 + x_1^2 + x_2^2 + x_3^2}
$$

Normalized vector:

$$
\vec{x}_{norm} = \left( \frac{x_0}{\|\vec{x}\|}, \frac{x_1}{\|\vec{x}\|}, \frac{x_2}{\|\vec{x}\|}, \frac{x_3}{\|\vec{x}\|} \right)
$$

---

### 5.3 Quantum State Representation  

The encoded quantum state is:

$$
|\psi\rangle =
\frac{x_0}{\|\vec{x}\|}|00\rangle +
\frac{x_1}{\|\vec{x}\|}|01\rangle +
\frac{x_2}{\|\vec{x}\|}|10\rangle +
\frac{x_3}{\|\vec{x}\|}|11\rangle
$$

---

## 6. Manual State Preparation Using Rotation Gates  

### 6.1 Motivation  

Quantum hardware does not allow arbitrary amplitude assignment directly.  
Instead, we use **quantum gates** to transform $|00\rangle$ into the desired state.

---

### 6.2 Step-by-Step Strategy  

We exploit:
- Single-qubit rotations
- Controlled rotations
- Tensor product structure

---

### 6.3 Decomposition Logic  

We rewrite the state as:

$$
|\psi\rangle =
\cos(\theta_1)|0\rangle|\phi_0\rangle +
\sin(\theta_1)|1\rangle|\phi_1\rangle
$$

Where:

$$
|\phi_0\rangle = \cos(\theta_2)|0\rangle + \sin(\theta_2)|1\rangle
$$

$$
|\phi_1\rangle = \cos(\theta_3)|0\rangle + \sin(\theta_3)|1\rangle
$$

---

### 6.4 Computing Angles  

Let:

$$
a = \sqrt{x_0^2 + x_1^2}
$$

$$
b = \sqrt{x_2^2 + x_3^2}
$$

Then:

$$
\theta_1 = 2 \arccos(a)
$$

$$
\theta_2 = 2 \arccos\left(\frac{x_0}{a}\right)
$$

$$
\theta_3 = 2 \arccos\left(\frac{x_2}{b}\right)
$$

---

### 6.5 Gate Sequence  

1. Apply $R_y(\theta_1)$ on qubit 0
2. Apply controlled-$R_y(\theta_2)$ (control: qubit 0)
3. Apply controlled-$R_y(\theta_3)$ (control: qubit 0)

This prepares the full amplitude-encoded state.

---

## 7. Visualization of Quantum States  

### 7.1 Statevector Representation  

The quantum state can be visualized as:

$$
|\psi\rangle =
\begin{bmatrix}
\alpha_0 \\
\alpha_1 \\
\alpha_2 \\
\alpha_3
\end{bmatrix}
$$

Where:

$$
|\alpha_i|^2 = \text{Probability of measuring } |i\rangle
$$

---

### 7.2 Bloch Sphere Limitation  

- Single qubit → Bloch sphere visualization
- Multi-qubit → Requires statevector or density matrix plots

---

## 8. Verification Using Quantum Simulation  

### 8.1 Simulation Workflow  

1. Build the circuit
2. Simulate using a statevector simulator
3. Extract amplitudes
4. Compare with normalized classical vector

---

### 8.2 Correctness Condition  

The encoding is correct if:

$$
|\alpha_i - x_i| < \epsilon
$$

For all $i$, where $\epsilon$ is numerical tolerance.

---

## 9. Computational Complexity  

| Aspect | Cost |
|-----|-----|
| Qubits | $\log_2(N)$ |
| Gates (general case) | $O(N)$ |
| Memory | Exponential advantage |

---

## 10. Limitations of Amplitude Encoding  

- Expensive state preparation
- Sensitive to noise
- Requires normalization
- Hard to implement on NISQ hardware

---

## 11. Applications  

- Quantum Machine Learning
- Quantum PCA
- HHL Algorithm
- Quantum classifiers
- Kernel methods

---

## 12. Summary  

- Quantum data encoding bridges classical and quantum computation
- Amplitude encoding offers exponential compression
- A 4D vector fits naturally into 2 qubits
- Manual state preparation relies on rotation and controlled gates
- Simulation verifies correctness

---

## 13. Key Takeaway  

> **Amplitude encoding transforms data into probability amplitudes — unlocking the true power of quantum parallelism.**

---

**Written By** : Shreya Palase(codeQubit)

**Date** : 19-Dec-2025

Thank you anf Keep Learning!
