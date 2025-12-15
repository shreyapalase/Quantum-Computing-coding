# Day20 Notes- Bell State Circuit on IBM-Style Real Backend  


## 1. Introduction

Quantum entanglement is one of the most fundamental and non-classical phenomena in quantum mechanics. Bell states represent the simplest and most widely studied examples of entangled quantum states. These states play a crucial role in quantum communication, quantum cryptography, quantum teleportation, and benchmarking quantum hardware.

In this practical, we study the preparation and measurement of a Bell state and analyze how **noise**, specifically the **depolarizing noise model**, affects the behavior of the quantum system. Simulations are performed using the **Aer simulator**, which can emulate both ideal and noisy IBM Quantum hardware.

---

## 2. Bell States Overview

Bell states are maximally entangled two-qubit quantum states. There are four standard Bell states:

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

$$
|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

$$
|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}
$$

$$
|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

In this practical, we focus on the **$|\Phi^+\rangle$ Bell state**, which exhibits perfect correlation between the two qubits when measured in the computational basis.

---

## 3. Mathematical Representation of the $|\Phi^+\rangle$ State

The Bell state $|\Phi^+\rangle$ is defined as:

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

This state cannot be written as a product of two independent single-qubit states, confirming that it is **entangled**. Measurement of one qubit immediately determines the outcome of the other qubit.

---

## 4. Conceptual Bell State Preparation

The conceptual steps to prepare the $|\Phi^+\rangle$ Bell state are:

1. Initialize both qubits in the ground state $|0\rangle$
2. Apply a Hadamard operation to the first qubit to create superposition
3. Apply a Controlled-NOT (CNOT) gate with the first qubit as control and the second as target

This process entangles the qubits and produces the Bell state.

---

## 5. Measurement of the Bell State

When measured in the computational (Z) basis:

- The outcomes $|00\rangle$ and $|11\rangle$ occur with equal probability
- The outcomes $|01\rangle$ and $|10\rangle$ ideally do not occur

Mathematically, the probabilities are:

$$
P(00) = P(11) = \frac{1}{2}
$$

$$
P(01) = P(10) = 0
$$

These correlations are a direct signature of quantum entanglement.

---

## 6. Ideal vs Real Quantum Hardware

### Ideal Quantum Simulation

In an ideal quantum simulator:

- Gates are perfect
- No decoherence is present
- Measurements are error-free

As a result, Bell state correlations match theoretical predictions exactly.

---

### Real IBM Quantum Hardware

Real quantum hardware experiences:

- Gate errors
- Decoherence
- Measurement (readout) errors
- Crosstalk between qubits

To study these effects without running on actual hardware, **noise models** are introduced in simulations.

---

## 7. Noise in Quantum Computing

Noise represents unwanted interactions between a quantum system and its environment, leading to loss of quantum information.

Common types of quantum noise include:

- Depolarizing noise
- Amplitude damping
- Phase damping
- Readout errors

In this practical, we focus on **depolarizing noise**, which provides a general approximation of hardware imperfections.

---

## 8. Depolarizing Noise Model

### Definition

The depolarizing noise model assumes that with a certain probability, the quantum state is replaced by a completely mixed state.

For a single qubit, the depolarizing channel is given by:

$$
\rho \rightarrow (1 - p)\rho + p\frac{I}{2}
$$

Where:
- $\rho$ is the density matrix of the qubit  
- $p$ is the depolarizing probability  
- $I$ is the identity operator  

---

### Physical Interpretation

Depolarizing noise represents random errors that completely scramble the quantum state, making all basis states equally likely. It captures the cumulative effect of unknown noise sources.

---

### Single-Qubit Depolarizing Noise

For single-qubit gates:

- With probability $(1 - p)$, the gate operates correctly
- With probability $p$, the qubit becomes maximally mixed

This results in reduced coherence and degraded measurement outcomes.

---

### Two-Qubit Depolarizing Noise

Two-qubit gates, such as CNOT, are more error-prone. The depolarizing channel for two qubits is expressed as:

$$
\rho \rightarrow (1 - p)\rho + p\frac{I}{4}
$$

This type of noise significantly impacts entanglement quality.

---

## 9. Impact of Depolarizing Noise on Bell States

When depolarizing noise is present:

- The probabilities of $|01\rangle$ and $|10\rangle$ increase
- Correlations between qubits weaken
- Entanglement fidelity decreases
- The Bell state gradually approaches a classical mixed state

As noise increases, the quantum advantage is reduced.

---

## 10. Aer Simulator with Noise Models

The Aer simulator enables:

- Simulation of quantum circuits with configurable noise
- Emulation of IBM-style backend behavior
- Testing algorithms before executing on real hardware

Adding depolarizing noise allows realistic evaluation of Bell state preparation and measurement.

---

## 11. Practical Significance

Studying Bell states under depolarizing noise helps in:

- Benchmarking quantum hardware
- Understanding noise sensitivity of entanglement
- Developing error mitigation techniques
- Evaluating the robustness of quantum algorithms

---

## 12. Conclusion

The Bell state $|\Phi^+\rangle$ is a foundational example of quantum entanglement. While ideal simulations show perfect correlations, real quantum hardware introduces noise that degrades performance. The depolarizing noise model provides a simple yet effective approximation of real-world imperfections.

Using Aer simulations with depolarizing noise bridges the gap between theoretical quantum mechanics and practical IBM Quantum backends.

---

**Written By** : Shreya Palase

**Date** : 13-Dec-2025

Thank you and keep Learning!
