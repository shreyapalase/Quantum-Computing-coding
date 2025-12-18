# Day 23 Notes - QAOA Implementation for Maxcut Problem

In this  we will understand the **Quantum Approximate Optimization Algorithm (QAOA)** to solve the **Maxcut problem** on a simple graph using **Qiskit**.

The Maxcut problem is a combinatorial optimization problem where the objective is to partition the vertices of a graph into two subsets such that the number of edges between the two subsets is maximized.

We will walk through the following steps:
- Define a graph for the MaxCut problem
- Construct the cost and mixer Hamiltonians
- Implement the QAOA circuit
- Optimize parameters using a classical optimizer
- Evaluate and visualize the results

## Table of Contents
1. [Introduction](#introduction)
2. [MaxCut Problem Overview](#maxcut-problem-overview)
3. [QAOA Overview](#qaoa-overview)
4. [Mathematical Formulation](#mathematical-formulation)
5. [QAOA Algorithm Steps](#qaoa-algorithm-steps)
6. [Implementation with Qiskit](#implementation-with-qiskit)
7. [Results and Evaluation](#results-and-evaluation)
8. [Summary](#summary)

## Introduction

The Quantum Approximate Optimization Algorithm (QAOA) is an algorithm designed to solve combinatorial optimization problems on quantum computers. It is an approximation algorithm that can be used for various NP-hard problems, including MaxCut, as the problem can be represented as a graph.

QAOA combines quantum and classical resources, using quantum operations to generate superpositions and classical optimization to tune the parameters of quantum gates.

## MaxCut Problem Overview

In the **MaxCut problem**, we are given an undirected graph $G(V, E)$ where $V$ is the set of vertices and $E$ is the set of edges. We aim to partition the vertices into two subsets, \( S \) and \( T \), such that the number of edges between the two subsets is maximized.

Mathematically, the MaxCut problem can be formulated as:

$$
\text{MaxCut}(G) = \max \sum_{(u,v) \in E} \left( \frac{1 - z_u z_v}{2} \right)
$$

Where:
- $z_u \in \{ -1, 1 \}$ indicates whether vertex  $u$ is in subset $S$ or $T$.
- The objective function sums over the edges of the graph, counting an edge between vertices $u$ and $v$ if the vertices are in different subsets.

## QAOA Overview

QAOA is a hybrid quantum-classical algorithm that uses quantum circuits to approximate the solution to combinatorial optimization problems. It works by applying a combination of **cost Hamiltonian** and **mixer Hamiltonian** operators to the quantum state and optimizing the resulting parameters to maximize the objective function.

### Hamiltonians in QAOA

1. **Cost Hamiltonian ( $H_C$)**: This Hamiltonian encodes the optimization problem to be solved. For the MaxCut problem, the cost Hamiltonian represents the objective function and is given by:

$$
H_C = \sum_{(u,v) \in E} \frac{1 - z_u z_v}{2}
$$


   This operator ensures that the quantum system is driven towards states that correspond to cuts of the graph, with the goal of maximizing the number of edges crossing between subsets \( S \) and \( T \).

2. **Mixer Hamiltonian ($H_M$)**: The mixer Hamiltonian introduces randomness into the quantum state, allowing the algorithm to explore different solutions. In the case of MaxCut, a common choice for the mixer Hamiltonian is the sum of Pauli-X operators acting on each qubit, which helps the system explore a broad range of possible states:
$$
H_M = \sum_{u \in V} X_u
$$


   Where $X_u$ is the Pauli-X operator acting on qubit $u$.

## Mathematical Formulation

The goal of QAOA is to prepare a quantum state that encodes a solution to the MaxCut problem. To achieve this, we apply the cost and mixer Hamiltonians in layers. The quantum state evolves as follows:

$$
U(\gamma, \beta) = e^{-i \gamma H_C} e^{-i \beta H_M}
$$

Where:
- $\gamma$ and $\beta$ are the parameters that control the application of the cost and mixer Hamiltonians, respectively.
- $e^{-i \gamma H_C}$ applies the cost Hamiltonian to the quantum state, while $e^{-i \beta H_M}$ applies the mixer Hamiltonian.

By alternating between these two Hamiltonians, the quantum state evolves in a way that explores different possible solutions. The optimization parameters $\gamma$ and $\beta$ are updated through a classical optimizer to maximize the expected value of the cost function.

## QAOA Algorithm Steps

1. **Initialization**: The algorithm begins by initializing the quantum state to a uniform superposition of all possible configurations of the qubits. This is typically done by applying Hadamard gates to each qubit.

2. **Apply the Cost Hamiltonian**: For each edge in the graph, the quantum system evolves according to the cost Hamiltonian $H_C$, using the parameter $\gamma$ to control the strength of the evolution. This drives the quantum state toward solutions that maximize the objective function.

3. **Apply the Mixer Hamiltonian**: The mixer Hamiltonian $H_M$ is applied to the quantum state using the parameter $\beta$. This introduces randomness and allows the quantum system to explore different configurations, ensuring that the search space is adequately covered.

4. **Repeat for p layers**: Steps 2 and 3 are repeated for $p$ layers, where $p$ is a parameter that controls the depth of the quantum circuit. The choice of $p$ affects the algorithm's ability to explore the solution space, with larger values of \( p \) generally providing better solutions.

5. **Measure the Qubits**: After $p$ layers of evolution, the quantum state is measured. This collapses the quantum state into one of the possible solutions, with the measurement outcome corresponding to a specific partition of the graph.

6. **Classical Optimization**: A classical optimizer (such as gradient descent, COBYLA, or other methods) is used to find the optimal values of the parameters $\gamma$ and $\beta$. The optimizer seeks the parameter set that maximizes the expected value of the cost Hamiltonian.

## Implementation with Qiskit

The implementation of QAOA involves several key steps:
- **Define the graph**: We first define the graph that represents the MaxCut problem. This graph specifies the vertices and edges that will be used in the optimization.
- **Construct the Hamiltonians**: Next, we construct the cost and mixer Hamiltonians that encode the MaxCut problem. These Hamiltonians guide the quantum state towards solutions that correspond to the optimal cut.
- **Implement the QAOA circuit**: The QAOA circuit alternates between the application of the cost and mixer Hamiltonians. The circuit is defined with parameters $\gamma$ and $\beta$, which are optimized to maximize the objective function.
- **Optimize the parameters**: Classical optimization methods are employed to tune the parameters of the quantum circuit. The optimizer iteratively adjusts $\gamma$ and $\beta$ to maximize the expected value of the cost Hamiltonian.
- **Evaluate the results**: Finally, we evaluate the results of the quantum computation by measuring the qubits and visualizing the optimal cut found by the algorithm.

## Results and Evaluation

Once the QAOA algorithm has been implemented and the parameters optimized, the next step is to evaluate the results. The algorithm's output is typically a solution to the MaxCut problem, which is a partition of the graph's vertices. The quality of the solution can be measured by the number of edges that are cut by the partition, and this can be compared to the optimal solution.

Visualization techniques can be used to compare the quantum solution to classical methods. The quality of the solution often improves with the number of layers $p$, but the computational resources required also increase.

## Summary

In this notebook, we implemented the **Quantum Approximate Optimization Algorithm (QAOA)** to solve the **MaxCut problem**. We discussed the theoretical background of QAOA, the construction of the cost and mixer Hamiltonians, and the steps involved in implementing and optimizing the quantum circuit. 

QAOA is a powerful hybrid algorithm that combines quantum and classical resources to solve combinatorial optimization problems. While it offers significant potential for quantum computing, the algorithm's success depends on the careful tuning of its parameters and the optimization process. Further exploration and refinement of the algorithm will likely lead to improved results for large and complex optimization problems.

---

**Written By** : Shreya Palase

**Date** : 17-Dec-2025

Thank you and Keep learning!
