# Mini Project Report-**Adaptive Quantum Message Router (AQMR)**  
  
**Author:** ***Shreya Sunil Palase***  
**Date of Creation:** *7-Dec-2025*  

---

# **Table of Contents**

1. [Abstract](#abstract)
2. [Project Concept](#project-concept) 
3. [Psudocode](#psodocode)
4. [What we  will implemented](#what-we-will-implemented)
5. [AQMR Step-By-Step System Workflow](#aqmr-step-by-step-system-workflow)
6. [Post Processing routing logic](#post-processing-routing-logic) 
7. [Extract relevant bits](#extract-relevant-bits)
8. [plot Histogram](#plot-histogram)
9. [Interpretation of Result](#interpretation-of-result)
10. [Project Summary](#project-summary)
11. [Conclusion](#conclusion)
12. [future Scope](#future-scope)
13. [Acknowledgement](#acknowledgement)

---

## **Abstract**

The **Adaptive Quantum Message Router (AQMR)** is a hybrid quantum‐information workflow designed to demonstrate how multi–qubit entanglement,
oracle‐based decision logic, superdense coding, and quantum teleportation can be integrated to route quantum messages adaptively.This report provides a structured, 
step-wise breakdown of the conceptual design, circuit components, execution pipeline, and interpretation of results for a full 7-qubit AQMR system.

---

## **Project Concept**
### Nodes
we'll created a 3-node quantum network:
- **A** = Sender
- **R** = Router(our smart algorithm)
- **B** = Receiver

### Goal
Node A wants to send a 2-bit message to B using the best method choosen by the router R.
**Two Possible transmission modes**:

1. Superdense Coding(faster but required good entanglement resource)
2. Teleportation(slower but reliable)

### Router's Task
Before transmitting .Router R uses a Deutsch-Jozsa-Style oracle check to determinesif the shared entanglement between A and B is:
- **Balanced(good entanglement)**: use superdense coding
- **Constant(low entanglement/noisy)**: use Teleportation

---
## Psudocode
-  step 1 :create Bell pair between A and B.
-  Step 2 : Introduced noisy switch
    - Use a controlled -unitary on B's qubit to optionally degrade entanglement(simulate network noise).
    - Router R does NOT know wether noise is present.
- Step 3 : Deutsch-Jozsa-Style oracle
    - Router R prepare an ancilla qubit.
    - oracle checks the "type" of entanglement
        - controlled NOTs
        - Controlled-Z
        - A multi-controlled gate to detect correaltion pattern.
    - router extract one Qubit to determine whether entanglement is balanced or constant.
- Step 4 :conditional routing(our controlled logic)
  - if entanglement is good ,R triggred superdense coding.
  - if entanglent is not good ,R triggered Teleportation coding
- Step 5 : Encode & Send Message
  - **for superdence coding**: A encodes 2 classical bits into 1 qubit.
  - ** for teleportation** : A teleport 1 qubit containing the message state.
- Step 6 : Receiver Decodes
  - if superdense coding was used -->  B applies Bell-Basis decoding. 
  - if Teleportation was used -->  B applies teleportation recovery opearation.
- Step 7 : Verify correctness
  - Print Measurement result.
  - Confirm that the router made the correct routing decision.
  - Confirms that the message was received correctly.

---

## What we will implemented 
1. Multi-Qubit Entangled State
2. Deutsch–Jozsa Style Oracle
3. Decision Logic Using Controlled Gates
4. Superdense Coding Protocol
5. Quantum Teleportation Protocol
6. Hybrid Quantum routing based on entanglement characteristics.

---

 ## AQMR System Workflow (Full 7-Qubit Process Step-by-Step) 

### **Step 1 — Qubit Allocation (7 Qubits)**
- **QuantumRegister**:
Create 7 qubits ,each with a specific role in the system:

| qubit | Purpose |
|------ | ------- |
| q0    | Teleportation message qubit |
| q1    | Suprdense coding sender qubit |
| q2    | superdense coding receiver qubit|
| q3    | Oracle Qubit(decision making |
| q4    | Teleportation entanglement qubit |
| q5    | Teleportation entanglement qubit|
| q6    | router qubit decide protocol path |

- **ClassicalRegister**:
  - c_superdense --> 2 bits
  - c_teleport --> 2 bits
  - c_oracle --> 1 bits
  - c_router  --> 1 bits
  - c_final  --> 6 bits(collect all measurement combinr analysis)
  ---

### **Step 2 — Create Bell Pair + Add Noise Switch**
we will perform two major task in this steps:
1. create a bell pair between sender(q1) and receiver(q2)
2. Add a controllable "noise switch" using qubit 4(this will degrade entanglement when turn on)
  ---

### **Step 3 — Prepare Multi-Qubit Entanglement**
**3.1 Superdense Coding Bell Pair**
- **Goal**: Create entanglement between sender(q[1]) and receiver(q[2]) for superdense coding.
**3.2 Teleportation Channel**
- **Goal** : Prepare entanglement between sender (q[0]) and receiver (q[5]) through ancillary qubits propagated the state q[0].
  
  ---

### **Step 4 — Oracle & Router Design**
- **Oracle(q[3])** : decides protocol path dynamically.H gate creates superposition 50% chance for router =0 or 1. cnot from oracle to router propogate decision.
- **Router(q[6])** : Acts as quantum control switch.router=0 then Teleportation executed, if router = 1 then superdense coding executed.

  ---

### **Step 5 — Superdense Coding Encoding**
- Classical message encoding:
  - example: message =10 --> encoded on q[1] using X and H gates.
each opeartion encodes 2 classical bits onto the entangled bell pair.actual path is decided later by reading the router qubit.

  ---

### **Step 6 — Teleportation Protocol**
Transfer q[0] state to q[5] using entanglement.
- q[4] and q[5] form the teleportation channel.
- q[0] intracts with q[4] ,propogating its state to q[5].
- Teleportation is verified in post processing.

  ---

### **Step 7 — Measurement**
Measure the all Qubit into c_final:

| Qubit | Classical Bit |
| ----- | ------------- |
| q3    | c_final[0] oracle |
| q6    | c_final[1] router |
| q1    | c_final[2] superdense bit 1 |
| q2    | c_final[3] superdense bit 2 |
| q0    | c_final[4] teleport bit 1 |
| q1    | c_final[5] teleport bit 2 |

  ---

### **Step 8 — Execute Circuit**
Circuit is run on simulator or hardware backend.
**Backend** : Qiskit(AerSimulator())
**shots** : 1024
**Purpose** : Simulate real quantum hardware behaivior and probabilistic outcome.

---

## **7. Post-Processing Routing Logic**
separate counts based on router qubit (c_final[1]):
- Router =1  --> Superdense coding path
- Router =0  --> Teleportation path
  
so we get our final circuit as for teleportation path :
<img width="1847" height="1655" alt="image" src="https://github.com/user-attachments/assets/fe985359-388f-4a49-8fcd-4245b2c87a17" />

---
  
##**8. Extract Relevant Bits**
Extract:  
- Superdense bits : c_final[2]+c_final[3]
- Teleportation bits : c_final[4] + c_final[5]
  
it hel to visulize only qubit relevant each protocol.

---

## **9. Plot Histogram**
Simulation output is visualized as a **counts histogram**, showing distribution over measured bitstrings.handles empty path gracefully (e.g ,if router = 1 never occure).
according to result we got histogram as following:
<img width="981" height="456" alt="image" src="https://github.com/user-attachments/assets/2b22ff7b-d80d-4131-aa40-a9bb72ce6a78" />

---

# **10. Interpretation of Results**
- Balanced oracle → Teleportation chosen  
- Constant oracle → Superdense coding chosen  
- Teleported states reconstructed correctly (within noise tolerance)  
- Superdense bits retrieved with high fidelity  
- Router adaptively switches channels as expected  

1. **Teleportation worked correctly**.the teleportation path qubits (c_final[4,5]) show the teleported states.
2. Two distinct teleportation outputs:
    - 00 - counts=504{253+251}
    - 11 - counts=520{268+252}

This states, our original quantum states being teleported probabilistically.slight imbalance due to simulation statistics(1024 shots).

---

## **11. Project Summary**

The **Adaptive Quantum Message Router (AQMR)** demonstrates an integrated use of core quantum communication concepts:

- **Multi-qubit entanglement** for global state correlation  
- **Deutsch–Jozsa oracle** for adaptive decision-making  
- **Superdense coding** for high-efficiency classical message delivery  
- **Quantum teleportation** for state transfer  
- **Controlled-gate logic** for conditional routing  
- **Measurement-driven post-processing** for final decoding

---

## **conclusion**-
The teleportation path is correctly seperated by router=0,The teleported qubit states appear as 00 or 11 with roughly eqaul probability.
consistent with original entangled input state.

---

## **Future Scope** 
AQMR illustrates how quantum networks can autonomously choose optimal communication channels based on quantum-computed properties of a function, highlighting a 
a future direction for adaptive quantum internet infrastructure.

---

## **Acknowedgement**
- Qiskit textbook(IBM Quantum)
- nielsen and chaung quantum computing
- Quantum communication protocol

---
**feel free to explore this project , but please do not copy or reuse the code or content without asking for permission first**
