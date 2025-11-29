# Day6 Notes - Measurement and Probability
this file provide you detailed notes about quantum measurement and probability to understand conept theoritically.

---

# Measurement and Probability in Quantum Computing

This document summarizes key theoretical concepts regarding measurement and probability in quantum mechanics, specifically as they apply to a single qubit.

---

## 1. Qubit Superposition

A fundamental principle of quantum mechanics is that a qubit can exist in a **superposition** of states. Unlike a classical bit, which must be either `0` or `1`, a qubit can exist in a state that is a linear combination of these two basis states:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

Here, $\alpha$ and $\beta$ are complex numbers called **amplitudes**.

## 2. The Measurement Collapse

The qubit remains in this superposition until it is **measured**. The act of measurement is an interactive process that irreversibly changes the state of the qubit.

*   When a measurement is performed, the superposition state **collapses** instantaneously into a single, definitive classical state: either $|0\rangle$ or $|1\rangle$.
*   The outcome of a single measurement is probabilistic; we cannot determine with certainty whether it will be `0` or `1` just by knowing $\alpha$ and $\beta$.

## 3. Probabilities from Amplitudes

The amplitudes $\alpha$ and $\beta$ govern the probability of a specific outcome upon measurement.

*   The probability of measuring the state $|0\rangle$ is given by the squared magnitude of its amplitude:
    $$
    P(0) = |\alpha|^2
    $$
*   The probability of measuring the state $|1\rangle$ is given by the squared magnitude of its amplitude:
    $$
    P(1) = |\beta|^2
    $$
*   Since the qubit must collapse to one of these two states, the probabilities must sum to 1:
    $$
    P(0) + P(1) = |\alpha|^2 + |\beta|^2 = 1
    $$

## 4. More Measurements Lead to Better Probability Distributions

A single measurement only yields one result (e.g., `0`). To verify the theoretical probabilities $P(0)$ and $P(1)$, one must run the quantum circuit multiple times (perform many "shots").

*   **Few Measurements:** A small number of measurements provide a noisy estimate of the true probability distribution.
*   **More Measurements:** As the number of measurements (shots) increases, the observed frequency of outcomes (`0` vs. `1`) converges towards the theoretical probabilities $|\alpha|^2$ and $|\beta|^2$. This process allows us to experimentally determine the quantum state's characteristics.

## 5. Measurement Bases: Z-Basis and X-Basis

The outcome of a measurement depends fundamentally on the **basis** in which the measurement is performed. A measurement basis defines the set of orthogonal states into which the qubit can collapse. You have learned two primary bases:

### Z-Basis (Computational Basis)

This is the standard measurement basis. It uses the states $|0\rangle$ and $|1\rangle$ as its reference points.

*   **Measurement outcomes:** The qubit collapses to either $|0\rangle$ or $|1\rangle$.
*   **Example:** Measuring a state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ in the Z-basis yields `0` with probability $|\alpha|^2$ and `1` with probability $|\beta|^2$.

### X-Basis (Hadamard Basis)

This basis uses a different set of orthogonal states: the plus state $|+\rangle$ and the minus state $|-\rangle$.

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \quad |-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
$$

---
**Written by**: Shreya Palase

**Date** : 27-Nov-2025

Thank you and Keep learning.

*   **Measurement outcomes:** The qubit collapses to either $|+\rangle$ or $|-\rangle$.
*   **Relationship to Z-Basis:** You can effectively measure in the X-basis by applying a Hadamard ($H$) gate to the qubit *before* measuring it in the standard Z-basis. The $H$ gate transforms the X-basis states into Z-basis states ($H|+\rangle = |0\rangle$, $H|-\rangle = |1\rangle$).
