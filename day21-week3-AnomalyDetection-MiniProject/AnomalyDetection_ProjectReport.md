# Mini Project Report - **Quantum-Assisted Anomaly Detection in Noisy Environment Sensor Networks**

**Name:** *Shreya Sunil Palase*  
**Subject:** *Quantum Computing*  
**Date:** *14-Dec-2025*  

---

## **Index**


1. Project Goal  
2. Introduction  
3. Background and Motivation  
4. System Architecture Overview  
5. Working Process  
6. Quantum Algorithms Used  
7. Quantum Circuit Diagram Description  
8. Simulation Setup  
9. Ideal vs Noisy Results Comparison  
10. Final Output and Observations  
11. Conclusion  
12. Summary  

---

## **1. Project Goal**

The objective of this project is to design and simulate a **noise-aware quantum workflow** capable of anomaly detection in environmental sensor networks. The system is designed to:

- Model environmental sensor data  
- Handle noise and uncertainty  
- Detect rare anomalous events  
- Operate under **NISQ-era hardware constraints**

---

## **2. Introduction**

Environmental monitoring systems rely heavily on distributed sensor networks. These systems generate large volumes of noisy and correlated data, making classical anomaly detection challenging. Quantum computing introduces new computational primitives such as **superposition**, **entanglement**, and **amplitude amplification**, which can improve the detection of rare events.

---

## **3. Background and Motivation**

Quantum devices currently operate in the **Noisy Intermediate-Scale Quantum (NISQ)** era. These devices suffer from decoherence and gate errors, which must be accounted for when designing real-world quantum algorithms.

---

## **4. System Architecture Overview**

The quantum-assisted anomaly detection framework consists of:

- Quantum encoding of sensor data  
- Entanglement for modeling correlated sensors  
- Noise modeling using depolarizing channels  
- Phase estimation for reliability assessment  
- Grover search for anomaly detection  

---

## **5. Working Process**

The complete workflow is divided into multiple structured steps, each representing a quantum processing stage under realistic conditions.

---

## **6. Quantum Algorithms Used**

### **Step 1: Encoding Environmental Sensor Data**

Sensor data is encoded into a two-qubit quantum state. Hadamard gates are applied to create a uniform superposition:

$$
|0\rangle \xrightarrow{H} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

For two qubits:

$$
|00\rangle \xrightarrow{H^{\otimes 2}} \frac{1}{2} (|00\rangle + |01\rangle + |10\rangle + |11\rangle)
$$

---

### **Step 2: Modeling Correlated Sensors Using Entanglement**

A Bell state is created to represent correlated sensor readings:

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
$$

This is achieved using a Hadamard gate followed by a CNOT gate.

---

### **Step 3: Introducing Sensor and Hardware Noise**

A depolarizing noise model is applied to simulate realistic quantum and sensor noise:

$$
\rho \rightarrow (1 - p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)
$$

where \( p \) represents the noise probability.

---

### **Step 4: Phase Estimation for Data Reliability Check**

Quantum Phase Estimation (QPE) is used to estimate the phase \( \phi \) associated with a unitary operator \( U \):

$$
U|\psi\rangle = e^{2\pi i \phi}|\psi\rangle
$$

The estimated phase provides insight into data stability.

---

### **Step 5: Quantum Fourier Transform (QFT) Interpretation**

The inverse QFT is applied to extract phase information:

$$
|k\rangle \rightarrow \frac{1}{\sqrt{2^n}} \sum_{j=0}^{2^n-1} e^{2\pi i k j / 2^n} |j\rangle
$$

This helps distinguish anomalous sensor behavior.

---

### **Step 6: Defining the Anomaly Oracle**

The oracle marks anomalous states by phase inversion:

$$
O_f |x\rangle = (-1)^{f(x)} |x\rangle
$$

where \( f(x) = 1 \) denotes an anomaly.

---

### **Step 7: Grover Diffusion Operator**

The Grover diffuser amplifies anomaly states:

$$
D = 2|\psi\rangle \langle \psi| - I
$$

---

### **Step 8: Grover Circuit for Anomaly Detection**

After \( k \) Grover iterations, the probability of measuring an anomalous state increases significantly:

$$
k \approx \frac{\pi}{4} \sqrt{N}
$$

---

### **Step 9: Running on Noisy Simulation**

The full circuit is executed using a noisy quantum simulator incorporating depolarizing noise and measurement errors.

---

### **Step 10: Ideal vs Noisy Comparison**

The output distributions from ideal and noisy simulations are compared to evaluate robustness.

---

## **8. Quantum Circuit Diagram Description**

The quantum circuit includes:
- Initialization using Hadamard gates  
- Entanglement using CNOT gates  
- Noise channels  
- Phase estimation sub-circuits  
- Grover oracle and diffuser
  <img width="820" height="238" alt="image" src="https://github.com/user-attachments/assets/0899798d-63c0-49be-a999-38a73e86092c" />


---

## **9. Simulation Setup**

- **Platform:** Qiskit AerSimulator  
- **Qubits:** 2–4  
- **Noise Model:** Depolarizing channel  
- **Shots:** Multiple runs for statistical analysis  
<img width="629" height="470" alt="image" src="https://github.com/user-attachments/assets/39c1a547-26e2-45d9-8504-87f20e613952" />

---

## **10. Ideal vs Noisy Results Comparison**

| Metric | Ideal Simulation | Noisy Simulation |
|------|-----------------|------------------|
| Anomaly Probability | High | Reduced |
| Stability | Strong | Fluctuating |
| Error Impact | None | Present |

---

## **11. Final Output and Observations**
**Expected Output**:
1. **Ideal** - |11> approximately 90 -100%
2. **Noisy** - |11> approximately 50 - 70%

Means Noise degrades entanglement and amplification ,confirms necessity of noise -aware algorithms.
- Grover amplification successfully highlights anomalous states |11>
- Noise reduces detection confidence  
- Phase estimation improves reliability assessment  

---

## **12. Conclusion**

This mini project demonstrates that quantum-assisted anomaly detection remains viable even under NISQ-era noise constraints. While performance degrades in noisy environments, the combination of entanglement, phase estimation, and Grover search offers a promising framework.

---

## **13. Summary**

- Designed a noise-aware quantum anomaly detection workflow  
- Modeled realistic sensor noise  
- Implemented core quantum algorithms  
- Compared ideal and noisy execution  

---

### **Future Scope**

- Scaling to larger sensor networks  
- Hybrid quantum–classical models  
- Execution on real quantum hardware  

---
Thank You!
