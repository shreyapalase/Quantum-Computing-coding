# day16 Notes  : Grover's Algorithm — 2-Qubit Search (N = 4)

This document explains Grover’s Search Algorithm for a 2-qubit quantum system, which corresponds to a search space of N = 4 possible states. The goal is to locate a single marked (target) state more efficiently than classical search.

---

## Overview

Grover’s Algorithm provides a quadratic speed-up for unstructured search problems.  
For N = 4, a classical search requires on average 2 queries, whereas Grover’s Algorithm needs only one iteration.

---

## 1. Prepare an Equal Superposition

We start with the initial quantum state:

$$|00\rangle$$

To create an equal probability distribution over all basis states, Hadamard gates are applied to both qubits:

$$H^{\otimes 2}|00\rangle = \frac{1}{2} (|00\rangle + |01\rangle + |10\rangle + |11\rangle)$$

This produces a uniform superposition of all four states.

---

## 2. Oracle: Marking the Target State

The oracle marks the desired target state by flipping its phase.  
If the marked state is represented by $$|x_t\rangle$$, the oracle performs:

$$|x_t\rangle \rightarrow -|x_t\rangle$$

Example: If the target is $$|10\rangle$$, then after applying the oracle the state becomes:

$$\frac{1}{2} (|00\rangle + |01\rangle - |10\rangle + |11\rangle)$$

Only the phase changes; probabilities remain unchanged at this stage.

---

## 3. Diffusion Operator (Amplitude Amplification)

The diffusion operator amplifies the amplitude of the marked state.  
It is defined as:

$$D = 2|\psi\rangle\langle\psi| - I$$

where

$$|\psi\rangle = H^{\otimes 2}|00\rangle$$

This operator inverts all amplitudes about their average, increasing the marked amplitude and decreasing the others.  
For a 2-qubit system (N = 4), a single diffusion step is enough to strongly amplify the correct state.

---

## 4. Amplitude Visualization

After performing the oracle and diffusion steps:

- The oracle applies a negative phase to the target state.  
- The diffusion operator lifts that marked amplitude above the rest.  
- A visualization would show one amplitude clearly dominating the others.

---

## 5. Measurement

A final measurement collapses the quantum state into one of the four basis states.  
Due to amplification, the marked state has the highest probability of being observed.

For N = 4, one full Grover iteration (oracle + diffusion) yields a high probability of success.

---

# Summary

Grover’s Algorithm for a 2-qubit search involves:

1. Creating an equal superposition  
2. Applying the oracle to flip the phase of the target state  
3. Applying the diffusion operator to amplify the target amplitude  
4. Observing the change in amplitudes  
5. Measuring to obtain the marked state  

The algorithm works by using quantum interference to suppress incorrect answers and amplify the correct one, providing a quadratic speed-up over classical methods.

---

**Written By:** Shreya Palase

**Date** : 9-Dec-2025
