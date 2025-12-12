#  Day19 Notes - Quantum Noise Simulation with Qiskit (AerSimulator Noise Model)

This document contains **deep theoretical notes** on quantum noise and simulation using Qiskit AerSimulator.  

---

## 1. What is Quantum Noise?

Quantum noise refers to the unavoidable disturbances and errors that affect quantum states during their creation, manipulation, and measurement. Quantum systems are extremely sensitive to their surroundings; even minimal interaction with the environment can degrade or destroy the delicate properties (superposition and entanglement) required for quantum computing.

### Why does noise occur in quantum systems?

1. **Interaction with environment (Decoherence):**  
   Qubits are never perfectly isolated and interact with environmental factors such as temperature, electromagnetic fields, and phonons, causing:
   - Loss of phase information (dephasing)  
   - Decay of excited states (relaxation)  

2. **Imperfect control operations:**  
   Physical gate implementations (microwave pulses, laser manipulations) introduce:
   - Over-rotation or under-rotation  
   - Timing errors  
   - Unwanted qubit-qubit coupling  

3. **Measurement imperfections:**  
   Amplification of weak quantum signals introduces:
   - Readout errors  
   - Misidentification of |0⟩ and |1⟩  

**Consequences of quantum noise:**  
- Reduced fidelity of quantum states  
- Decreased accuracy in quantum circuits  
- Loss of entanglement and coherence  
- Accumulation of errors with increasing circuit depth  

---

## 2. Types of Quantum Noise (Focus on Key Models)

Quantum noise is mathematically described using **quantum channels** and **Kraus operators**. Below are the primary types used in quantum simulation:

---

### 2.1. Bit-Flip Noise

**Definition:** Random flips between |0⟩ ↔ |1⟩ with probability \(p\).  

**Kraus Operators:** 

$$
K_0 = \sqrt{1-p} I, \quad K_1 = \sqrt{p} X
$$

**Effect:**  
- |0⟩ → |1⟩ and |1⟩ → |0⟩ probabilistically  
- Represents errors in computational states  

**Physical Example:** Spontaneous qubit flips due to environmental disturbances or imperfect gates.

---

### 2.2. Phase-Flip Noise

**Definition:** Flips the phase of |1⟩ without changing |0⟩, causing decoherence in superpositions.  

**Kraus Operators:**  

$$
K_0 = \sqrt{1-p} I, \quad K_1 = \sqrt{p} Z
$$

**Effect:**  
- Superposition states (e.g., |+⟩) lose coherence  
- Computational states |0⟩ or |1⟩ remain unchanged  

**Physical Example:** Dephasing from environmental fluctuations, magnetic noise.

---

### 2.3. Depolarizing Noise

**Definition:** Qubit is replaced by a completely mixed state with probability \(p\). Represents uniform random errors.  

**Mathematical Form:**  

$$
\rho \to (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)
$$

**Effect:**  
- Qubit state moves toward maximally mixed state  
- Both population and phase information are reduced  

**Physical Example:** Imperfect gate implementations and general random perturbations.

---

### 2.4. Amplitude Damping Noise

**Definition:** Models energy loss from |1⟩ → |0⟩ (relaxation).  

**Kraus Operators:**  

$$
K_0 = \begin{bmatrix}1 & 0 \\ 0 & \sqrt{1-\gamma}\end{bmatrix}, \quad K_1 = \begin{bmatrix}0 & \sqrt{\gamma} \\ 0 & 0\end{bmatrix}
$$

**Effect:**  
- Excited states |1⟩ decay to |0⟩  
- Superpositions lose amplitude of |1⟩, reducing coherence  

**Physical Example:** Relaxation in superconducting qubits or trapped ions.

---

### 2.5. Phase Damping Noise (Dephasing)

**Definition:** Loss of phase coherence without changing |0⟩ or |1⟩ populations.  

**Kraus Operators:**  

$$
K_0 = \sqrt{1-\lambda} I, \quad K_1 = \sqrt{\lambda} |0\rangle \langle 0|, \quad K_2 = \sqrt{\lambda} |1\rangle \langle 1|
$$

**Effect:**  
- Superposition states decay to classical mixtures  
- Populations remain unchanged  

**Physical Example:** Dephasing caused by environmental fluctuations, magnetic noise, or nearby qubits.

---

**Summary Table:**

| Noise Type | Main Effect | Key Feature | Kraus Representation |
|-----------|-------------|------------|--------------------|
| Bit-Flip | Flip | Changes computational state |K₀=√(1-p)I, K₁=√pX |
| Phase-Flip | Phase change | Coherence loss | K₀=√(1-p)I, K₁=√pZ |
| Depolarizing | Mix | Random X/Y/Z error | ρ→(1-p)ρ + p/3(XρX+YρY+ZρZ) |
| Amplitude Damping | Relaxation | Energy loss | K₀=[[1,0],[0,√1-γ]], K₁=[[0,√γ],[0,0]] |
| Phase Damping | Dephasing | Phase loss only | K₀=√(1-λ)I, K₁=√λ |

---

## 3. How to Simulate Noise using Qiskit AerSimulator

**Qiskit Aer** allows simulation of realistic hardware noise using:

1. **Noise Channels:** Define specific errors for gates, measurements, and qubits.  
2. **Simulator Integration:** AerSimulator can execute circuits with these noise models.  
3. **Execution:** The simulated output includes stochastic deviations caused by noise.  

**Purpose of Noise Simulation:**  
- Evaluate quantum algorithm performance on realistic hardware  
- Test error mitigation and fault-tolerance strategies  
- Identify gates or qubits most susceptible to noise  

---

## 4. Compare Ideal Simulation vs. Noisy Simulation

| Property | Ideal Simulation | Noisy Simulation |
|---------|-----------------|-----------------|
| Accuracy | Perfect | Reduced by noise |
| State Evolution | Unitary only | Stochastic channels included |
| Measurement | Exact | Possible misclassification |
| Purpose | Theoretical validation | Emulate hardware performance |

**Insights from Comparison:**  
- Shows fidelity loss due to noise  
- Reveals sensitivity of circuits to specific errors  
- Guides optimization and mitigation techniques  

---

## 5. Result and Future Scope

**Expected Results:**  
- Deviations between ideal and noisy outputs  
- Reduced fidelity of quantum states  
- Identification of critical noise sources in circuits  

**Future Scope:**  
1. **Quantum Error Mitigation:** Zero-noise extrapolation, probabilistic error cancellation  
2. **Quantum Error Correction:** Surface codes, stabilizer codes  
3. **Noise-aware Circuit Optimization:** Reduce depth, assign qubits to less noisy hardware  
4. **Hardware-efficient Designs:** Minimize gate count and optimize gate sequences  
5. **Noise Modeling and Prediction:** Machine learning-based adaptive noise models  

Noise simulation is a **critical step** for understanding limitations in NISQ devices and preparing for fault-tolerant quantum computing.

---

**Written By** : Shreya Palase

**Date** : 12-Dec-2025

Thank you and Keep Learning!
