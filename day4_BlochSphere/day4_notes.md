# Day4 Notes - Qubit and Bloch Sphere
Today we bulid strong intuition  for how **Qubits behave Geometrically**.

---

## What We Learn Today:
- Mathematical representation of **a Qubit**
- Geometric bloch sphere representation
- visualizing |0> and |1> as bloch vector
- Understanding **Superposition** using Bloch coordinates
- Applying Quantum gate(X,Y,H,Z) and seeing rotations
- creating **custom qubit state** using state(θ,φ)
- understanding rotation gates:**Rx,Ry,Rz**
- Phase changes and Bloch Z-axis rotations

---

## 1.What is a Qubit?
A  Qubit is 2-level quantum state represent as:
$$|\psi \rangle =\cos \left(\frac{\theta }{2}\right)|0\rangle +e^{i\phi }\sin \left(\frac{\theta }{2}\right)|1\rangle$$
Unlike classical bits ,qubits can be in **Superposition**.  
Example:  
- |0> = North pole of bloch Sphere
- |1> = South pole

  ---

  ## 2.Bloch Spere Representation
  Any Qubit can be mapped onto a point on the Bloch Sphere via angles:
  
  $$|\psi\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle$$

  - **θ** - lattitude(superposition amplitude)
  - **φ** - longitude(Phase)  
  This why Bloch sphere are the most intuitive way to undestand Qubit.

---

## 3.Visualizing Basis States
Using Qiskit |0> and |1> are correspond to :
- |0> - Bloch vector pointing UP
- |1> - Bloch vector pointing DOWN

---

## 4.Gate Effect on Bloch Sphere
Quantum gates Correspond to **Rotations**.

| Gate | Bloch Sphere Effect |
|------| ----------------------|
| **H** | Move |0> --> to equator(Superposition) |
| **X** | 180<sup>0</sup> rotation around X-axis |
| **Y** | 180<sup>0</sup> rotation around Y-axis |
| **Z** | 180<sup>0</sup>  rotation around Z-axis |
| **P(φ)** | adds phase to Z-axis rotations |
| **Rx** | Arbitray rotation around X-axis |
| **Ry** | Arbitray rotation around Y-axis |
| **Rz** | Arbitray rotation around Z-axis |

You visualize using  **plot_bloch_mulitivector(state)** in Python.

---

## 5.Creating custom Qubits(θ,φ)
You can create custom qubits by choosing θ and φ:

$$\alpha = \cos(\theta/2), \quad \beta = e^{i\phi}\sin(\theta/2)$$

Example:
**θ** = π/3 and **φ** = π/4  
**Normalization Check** : |α|<sup>2</sup> + |β|<sup>2</sup> = 1  
**Visual intuition** : 0 moves vector north-south ,φ rotates arounf z-axis.  
**Special Qubit states** : 
- |+> = (|0> +|1>)\ <sqrt>2</sqrt> --> equator ,φ = 0
- |-> = (|0> +|1>)\ <sqrt>2</sqrt> --> equator ,φ = π
- |i> = (|0> +i|1>)\ <sqrt>2</sqrt> --> equator ,φ = π/2

---

## 6.Rotation Gates(Rx ,Ry, Rz)
rotation gates allow arbitrary rotation:
- rx(π/2,0) --> rotates qubit around X-axis
- ry(π/2,0) --> rotates qubit around Y-axis
- rz(π/2,0) --> rotates qubit around Z-axis

---

## 7.Phase Gate Example
The **phase gate P(φ)**:

$$P(\phi) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\phi} \end{bmatrix}$$

- Only the **|1> component** changes phase
- appear as a rotation around the Z-axis
- useful for constructing relative phase difference in algorithm.

---

**refer above notes side by side while or before  executing 'day4_BlochSphere.ipynb' file for deep understanding.

---

**Written By** :Shreya Palase

**Date** : 27-Nov-2025

Thank you and Keep Learning.




