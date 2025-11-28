# Day5 Notes - Understanding and Simulating Qunatum Gates
 This file give detailed description of what is Quantum gate,How its work and how to Simualte using AerSimulator()

---
# What is Quantum Gate?
A Quantum Gate is a basic opeartion that changes the state of qubits .it it represented using unitary matrix and can manipulate qubits to create superposition ,entanglement or flips .All Quantum gate are reversible.there are many quantum gate .but basically X gate,Y gate,Z gate and H-gate etc. so let see them one by one.

---

# The Pauli-X Gate

The **Pauli-X gate**, often simply called the X gate, is a fundamental single-qubit quantum gate. It is the quantum analogue of the classical **NOT** logic gate.

## Action

When applied to a qubit, the X gate effectively "flips" the state of the qubit:

*   It maps the state $|0\rangle$ to $|1\rangle$.
*   It maps the state $|1\rangle$ to $|0\rangle$.

## Mathematical Representation

In linear algebra, the X gate is represented by a 2x2 unitary matrix. GitHub uses KaTeX to render math placed within single or double dollar signs.

$$
X = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

## Effect on Bloch Sphere

Visually, the X gate corresponds to a **$180^\circ$ (or $\pi$ radians) rotation around the X-axis** of the Bloch sphere.

It transforms the standard basis states as follows:

$$
X|0\rangle = |1\rangle
$$

$$
X|1\rangle = |0\rangle
$$

## Key Property

The X gate is its own inverse; applying it twice returns the qubit to its original state:

$$
X(X|\psi\rangle) = |\psi\rangle
$$

---

# The Pauli-Y Gate

The **Pauli-Y gate**, often referred to as the Y gate, is a fundamental single-qubit quantum gate that combines a bit flip and a phase flip.

## Action

The Y gate applies a transformation that can be understood as a bit flip followed by a phase shift of $i$.

*   It maps the state $|0\rangle$ to $i|1\rangle$.
*   It maps the state $|1\rangle$ to $-i|0\rangle$.

## Mathematical Representation

In linear algebra, the Y gate is represented by a 2x2 unitary matrix using imaginary numbers ($i = \sqrt{-1}$).

$$
Y = \begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}
$$

## Effect on Bloch Sphere

Visually, the Y gate corresponds to a **$180^\circ$ (or $\pi$ radians) rotation around the Y-axis** of the Bloch sphere.

It transforms the standard basis states as follows:

$$
Y|0\rangle = i|1\rangle
$$

$$
Y|1\rangle = -i|0\rangle
$$

## Key Properties

Like the X and Z gates, the Y gate is its own inverse ($Y^2 = I$).

It is closely related to the X and Z gates through the equation:

$$
Y = iXZ
$$

---

# The Pauli-Z Gate

The **Pauli-Z gate**, or Z gate, is a fundamental single-qubit quantum gate known primarily as a phase gate.

## Action

Unlike the X gate, the Z gate does not flip the computational basis states ($|0\rangle$ and $|1\rangle$). Instead, it applies a conditional **phase shift**.

*   It leaves the state $|0\rangle$ unchanged.
*   It applies a negative phase factor ($-1$) to the state $|1\rangle$.

## Mathematical Representation

In linear algebra, the Z gate is represented by a 2x2 unitary matrix:

$$
Z = \begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$

## Effect on Bloch Sphere

Visually, the Z gate corresponds to a **$180^\circ$ (or $\pi$ radians) rotation around the Z-axis** of the Bloch sphere.

It transforms the standard basis states as follows:

$$
Z|0\rangle = |0\rangle
$$

$$
Z|1\rangle = -|1\rangle
$$

## Key Properties

*   **Identity:** Like the X and Y gates, the Z gate is its own inverse ($Z^2 = I$).
*   **Hadamard Relationship:** The Z gate can be implemented using X gates and Hadamard gates: $Z = H X H$.
*   **Pauli Group:** The X, Y, and Z gates form the core of the Pauli group of operators, which are crucial for quantum error correction.

---

# The Hadamard Gate

The **Hadamard (H) gate** is one of the most important single-qubit quantum gates. Its primary function is to create a superposition of states.

## Action

The H gate transforms the computational basis states ($|0\rangle$ and $|1\rangle$) into an even superposition of both states:

*   It maps the state $|0\rangle$ to the $|+\rangle$ state.
*   It maps the state $|1\rangle$ to the $|-\rangle$ state.

## Mathematical Representation

In linear algebra, the Hadamard gate is represented by a 2x2 unitary matrix, scaled by a factor of $\frac{1}{\sqrt{2}}$:

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
$$

## Effect on Bloch Sphere

Visually, the H gate corresponds to a **$90^\circ$ rotation around the Y-axis, followed by a $180^\circ$ rotation around the X-axis** (or various equivalent rotations). Its key effect is moving states between the Z-axis (vertical: $|0\rangle, |1\rangle$) and the X-axis (horizontal: $|+\rangle, |-\rangle$).

It transforms the standard basis states as follows:

$$
H|0\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

$$
H|1\rangle = |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

## Key Properties

*   **Self-Inverse:** Applying the Hadamard gate twice returns the qubit to its original state ($H^2 = I$).
*   **Creating Superposition:** It is the standard gate used to place a single qubit into an equal superposition of $|0\rangle$ and $|1\rangle$ at the start of most quantum algorithms.
*   **Basis Change:** It acts as a change of basis operator between the computational Z-basis and the X-basis.

---

# The Ry($\pi/3$) Gate

This gate is a specific instance of the **Y-axis rotation gate** where the rotation angle $\theta$ is set to $\pi/3$ radians (60 degrees).

## Action

This gate applies a precise, partial rotation around the Y-axis of the Bloch sphere, changing the relative amplitudes of the $|0\rangle$ and $|1\rangle$ components of a qubit's state.

## Mathematical Representation

The general matrix for the $R_y(\theta)$ gate is:

$$
R_y(\theta) = \begin{pmatrix}
\cos\left(\frac{\theta}{2}\right) & -\sin\left(\frac{\theta}{2}\right) \\
\sin\left(\frac{\theta}{2}\right) & \cos\left(\frac{\theta}{2}\right)
\end{pmatrix}
$$

For $\theta = \pi/3$, the $\theta/2$ term becomes $\pi/6$. We use the trigonometric values $\cos(\pi/6) = \frac{\sqrt{3}}{2}$ and $\sin(\pi/6) = \frac{1}{2}$ to define the specific matrix:

$$
R_y(\pi/3) = \begin{pmatrix}
\cos\left(\frac{\pi}{6}\right) & -\sin\left(\frac{\pi}{6}\right) \\
\sin\left(\frac{\pi}{6}\right) & \cos\left(\frac{\pi}{6}\right)
\end{pmatrix}
=\begin{pmatrix}
\frac{\sqrt{3}}{2} & -\frac{1}{2} \\
\frac{1}{2} & \frac{\sqrt{3}}{2}
\end{pmatrix}
$$

## Effect on Qubit State

When applied to the initial state $|0\rangle$, the gate rotates it to a specific superposition state $|\psi\rangle$:

$$
R_y(\pi/3)|0\rangle = \frac{\sqrt{3}}{2}|0\rangle + \frac{1}{2}|1\rangle
$$

## Key Property

This gate is not self-inverse like the Pauli gates. To reverse this operation, you must apply the gate $R_y(-\pi/3)$, which rotates the qubit back by 60 degrees in the opposite direction.

---

# Summary of Fundamental Quantum Gates

This document provides a brief overview and mathematical representation of common single-qubit quantum gates discussed previously.for hands-on prectic refer **day5_QuantumGates.ipynb**.



---

* * *

**Written By:** Shreya Palase

**Date Generated:** November 28, 2025

Thank You and Keep Learning!
* * *

---



