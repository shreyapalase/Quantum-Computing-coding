# Day 24 Notes - Quantum Machine Learning (QML)

## Introduction

Quantum Machine Learning (QML) is an interdisciplinary field that combines **quantum computing** with **classical machine learning**. The core idea of QML is to explore how quantum mechanical principles such as **superposition**, **entanglement**, and **measurement** can be used to design learning algorithms.

In this notebook, we focus on building a **simple Quantum Neural Network (QNN)** for **binary classification** using only **core Qiskit tools**, without installing any additional Quantum Machine Learning libraries.

---

## Objectives of This Notebook

In this notebook, we aim to:

- Understand the basic idea of a **Quantum Neural Network (QNN)**
- Learn how to encode classical data into a **quantum circuit**
- Use **trainable quantum parameters** through variational circuits
- Perform **binary classification** using expectation values
- Implement a QNN **without using external QML libraries**

---

## Why Quantum Machine Learning?

Classical machine learning models rely on mathematical transformations applied to data using trainable parameters. Quantum Machine Learning explores whether quantum computers can improve or accelerate these tasks.

Quantum models leverage:
- Superposition to process multiple states simultaneously
- Entanglement to capture complex correlations
- Measurement to extract meaningful outputs

---

## Quantum Neural Network (QNN)

A Quantum Neural Network is a **variational quantum model** inspired by classical neural networks. Instead of neurons and activation functions, QNNs use **quantum gates and measurements**.

A typical QNN consists of:

1. A **data encoding circuit**
2. A **variational (trainable) quantum circuit**
3. A **measurement process** to obtain predictions

---

## Classical Data Encoding

### Feature Mapping

Classical data must be converted into quantum states before processing. This step is called **data encoding** or **feature mapping**.

For a classical feature vector:

$$
\mathbf{x} = (x_1, x_2, \dots, x_n)
$$

the goal is to map these values into a quantum state.

---

### Angle Encoding

Angle encoding is one of the simplest encoding techniques. Classical values are used as rotation angles for quantum gates.

For a single qubit, the encoded state is:

$$
|\psi(x)\rangle = R_y(x)\,|0\rangle
$$

This encoding ensures that classical information is embedded directly into the quantum state.

---

## Variational Quantum Circuits

### Definition

A **variational quantum circuit** is a quantum circuit containing **trainable parameters**, similar to weights in a classical neural network.

The quantum state after applying the variational circuit is:

$$
|\psi(\theta)\rangle = U(\theta)\,|\psi_{\text{encoded}}\rangle
$$

where:
- $U{\theta}$ is a parameterized unitary operation
- $\theta$ represents trainable parameters

---

### Trainable Parameters

Trainable parameters:
- Control quantum gate rotations
- Allow the model to learn from data
- Are optimized using classical optimization algorithms

This results in a **hybrid quantum–classical learning process**.

---

## Measurement and Expectation Values

### Quantum Measurement

Quantum states cannot be directly observed. Information is extracted through measurement using quantum observables.

The expectation value of an observable $O$ is given by:

$$
\langle O \rangle = \langle \psi | O | \psi \rangle
$$

For binary classification, the Pauli-Z observable is commonly used:

$$
\langle Z \rangle \in [-1, 1]
$$

---

### Decision Rule for Classification

The expectation value is converted into a class label using a threshold:

$$
\text{Class} =
\begin{cases}
1 & \text{if } \langle Z \rangle \ge 0 \\
0 & \text{if } \langle Z \rangle < 0
\end{cases}
$$

---

## Training the Quantum Neural Network

### Loss Function

To train the QNN, a loss function is defined to measure prediction error. A common choice is Mean Squared Error (MSE):

$$
L = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2
$$

where:
- $y_i$ is the true label
- $\hat{y}_i$ is the predicted value

---

### Optimization Process

The training procedure follows these steps:

1. Encode classical data into quantum states
2. Apply the variational quantum circuit
3. Measure expectation values
4. Compute loss using classical computation
5. Update parameters using a classical optimizer
6. Repeat until convergence

This is known as **hybrid quantum-classical optimization**.

---

## Binary Classification Using QNN

In this notebook, the QNN is designed for **binary classification**, meaning:
- There are only two output classes
- A single expectation value is used as output
- The decision boundary is simple and interpretable

---

## Advantages and Limitations

### Advantages

- Utilizes quantum superposition and entanglement
- Compatible with near-term quantum devices
- Requires only a small number of qubits
- Implemented using only **core Qiskit tools**

### Limitations

- Limited scalability
- Sensitive to quantum noise
- Small datasets
- No proven quantum advantage for most tasks yet

---

## Key Takeaways

- Quantum Neural Networks are **variational quantum models**
- Classical data is encoded into quantum states
- Trainable quantum gates act as learnable parameters
- Measurements provide model predictions
- Expectation values enable binary classification
- QNNs can be implemented without extra QML libraries

---

## Conclusion

This notebook demonstrates how **classical machine learning principles** can be implemented using **quantum circuits**. By building a simple Quantum Neural Network for binary classification using core Qiskit tools, we establish a strong theoretical foundation for understanding and exploring Quantum Machine Learning.


**Written by** : Shreya Palase

**Date**:18-Dec-2024

Thank you and keep learning!
