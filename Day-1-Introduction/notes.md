# Introduction to Quantum Computing

## 1.What is Quantum Computing?
 Quantum computing is the type of computing that uses principle of quantum mechanics to perform calculation.
 Unlike classical computers that use bits(0 or 1) ,quantum computers uses  qubits which cam exist in multiple state at once.

 ## 2.What is a Qubit?
 A qubit is the basic unit of quantum information.Unlike a classical bit:  
 1. classical bit can be either 0 or 1.
 2. a qubit can be superposition of 0 and 1 at the same time.
 Mathematically ,a qubit is represented as:
 ∣Ψ⟩=α∣0⟩+β∣1⟩
 Where:
 α =amplitude for∣0⟩
 β= amplitude for ∣1⟩
 ∣α∣<sup>2</sup>+∣β∣<sup>2</sup> =1 (probabilities sum to 1)

 ## 3.What is Superposition?
 Superposition allows a qubit to exist in multiple state simulteneously. A qubit can be partly 0 and partly 1.
 When measured  it collapse to either 0 or 1 with probabilities ∣α∣<sup>2</sup> and ∣β∣<sup>2</sup>. 

## 4.What is Measurement?
 Measurement force a qubit to choose a definite state (0 or 1).This is fundamentally different from classical bits, which are always
 deterministic.

## 5.What is Quantum gates?
 Quantum gates are operation that manipulate qubits.They are similar to logic gates in classical computing.
 for example - Hadamard gate ,Pauli-X-gate , CNOT gate etc. we will see this in detail later.

## 6.What is Quantum circuit?
A quantum circuit is a sequence of quantum gates applied to qubits.we can simulate these circuit using Python libraries such as qiskit.
example workflow:
1. create quantum circuit with qubit and classical bit.  
2. apply hadamard gate to put qubit in superposition.  
3. Measure the qubit.  
4. Visualize or draw the circuit.  

## 7.Key difference between classical Vs Quantum
- in classical computing basic unit include Bit(0 or 1) while in Qunatum computer basic unit is Qubit(Superposition).
- classical computer is deterministic while quantum computer are probabilistic.
- Classical computer having parellelism limited while quantum computer having parellelism high.
- Classical computer use gate AND,OR,NOT while Quantum computer using  gate H,X,CNOT.

## 8.Tool to Practice Quantum computing
- Python :Programming language  
- Jupiter notebook write and run code intractively.  
- Qiskit: Python library for simulating quantum circuit.  

## 9.Summery:
Todays you learned:
1. what a qubit is and the concept of superposition
2. Measurement of qubits
3. Basic of quantum gates and quantum circuit
4. Tools needed :Python ,Jupiter,Qiskit
5.How to create your first quantum circuit with hadamard gate and measurement.
