# Case Study: QAOA-Based Energy-Efficient Satellite Task Scheduling Under Orbital Visibility Constraints
<img width="1200" height="627" alt="wintchester-satelite-open-graph" src="https://github.com/user-attachments/assets/dc6384f0-886b-4c20-8a55-8cd31b7b2be0" />




---

## Abstract

This case study presents a simulation-based evaluation of a Quantum Approximate Optimization Algorithm (QAOA) applied to energy-efficient satellite task scheduling under orbital visibility constraints. The study is motivated by real-world low-Earth orbit (LEO) satellite missions, where limited onboard energy, restricted visibility windows, and competing task priorities pose significant operational challenges. A classical scheduling baseline and a quantum optimization approach are analyzed within a realistic mission context. Rather than repeating detailed algorithmic results, this case study focuses on interpreting previously obtained results at the mission level and assessing their implications for future satellite operations.

---

## 1. Mission Context and Motivation

Modern Earth observation satellites operate under stringent resource constraints. Each orbit provides only short visibility windows for task execution, while onboard energy must be carefully managed to ensure long-term mission sustainability.

Typical mission objectives include:
- High-resolution Earth imaging
- Environmental and agricultural monitoring
- Emergency and disaster response
- Satellite calibration and health diagnostics

Efficient scheduling is therefore essential to maximize mission value while minimizing energy consumption.

---

## 2. Case Study Scenario Description

### 2.1 Inspired Mission Type

This case study is inspired by real LEO Earth observation missions such as:
- Environmental monitoring satellites
- Remote sensing CubeSat platforms
- Small satellite technology demonstrators

The scenario models a **single satellite operating over multiple orbits**, executing tasks that are constrained by orbital visibility and energy availability.

---

### 2.2 Task and Constraint Modeling

The simulated mission considers a finite set of observation and operational tasks, each characterized by:
- Energy consumption cost
- Priority level
- Assigned orbital visibility window

The visibility windows are determined by orbital geometry, while energy costs reflect realistic payload and subsystem power usage.

> **Note:** The task parameters and constraints are synthetically generated but designed to reflect realistic satellite operations.

---

## 3. Scheduling Approaches Considered : Real-World Relevance to LEO Earth Observation Missions

### 3.1 Overview of LEO Earth Observation Satellites

Low Earth Orbit (LEO) Earth observation satellites typically operate at altitudes between **500 km and 800 km**. This orbital regime is widely used for remote sensing missions because it balances **high spatial resolution**, **short revisit times**, and **energy efficiency**.

Examples include:
- Sentinel-2 (ESA)
- Landsat-8/9 (NASA/USGS)
- PlanetScope CubeSat constellations

These satellites perform high-resolution Earth imaging, environmental monitoring, disaster assessment, and climate observation.

---

### 3.2 Operational Characteristics Relevant to Task Scheduling

#### Orbital Visibility Constraints
- Satellites can only observe a specific ground target for a **short duration** (tens of seconds to a few minutes per pass).  
- Limited observation periods create **visibility windows** during which tasks must be executed.  
- Missed windows cannot always be recovered until the next orbital pass.  

This maps directly to the **visibility windows (W1, W2, W3)** modeled in this project.

#### Energy Constraints
- Imaging payloads and communication systems consume significant onboard energy.  
- Satellites rely on **solar panels and batteries**, making energy management critical.  
- High-resolution imaging consumes more energy than routine calibration or monitoring tasks.  

The **energy costs assigned to tasks** in the project reflect these real operational constraints.

#### Priority-Driven Task Requests
- Mission planners assign priorities based on urgency and mission value.  
- Disaster monitoring or emergency response tasks are typically **high priority**, while calibration or routine monitoring are medium/low priority.  

This corresponds to the **task priority levels** (high, medium, low) in the project.

---

### 3.3 Classical Scheduling in Real Missions

- Most LEO missions use **rule-based or heuristic scheduling methods**.  
- Decisions are made independently for each orbital pass.  
- While efficient, these approaches are **local and myopic**, often leading to suboptimal energy usage across multiple passes.  

This is consistent with the **classical baseline algorithm** implemented in the project.

---

### 3.4 Relevance of QAOA-Based Scheduling

As LEO missions grow in complexity, classical scheduling methods face limitations. The QAOA-based scheduling in this project:
- Evaluates **global energy-priority trade-offs** across multiple visibility windows  
- Explores multiple scheduling combinations simultaneously  
- Provides probabilistic solutions that may **favor energy-efficient tasks**, even with lower classical priority  

This demonstrates how quantum optimization could enhance future autonomous satellite operations.

---

### 3.5 Mapping Real Missions to the Project Model

| Real LEO Mission Aspect      | Representation in Project                  |
|------------------------------|-------------------------------------------|
| Ground pass duration          | Visibility windows (W1, W2, W3)          |
| Power-hungry payloads         | Energy cost per task                       |
| Mission urgency               | Task priority levels                        |
| Orbit-to-orbit planning       | Window-based scheduling                     |
| Autonomous optimization       | QAOA-based decision-making                  |

This mapping confirms that the project is a **valid abstraction** of real LEO satellite scheduling.

---

### 3.6 Summary

LEO Earth observation satellites operate under **strict energy, visibility, and priority constraints** that closely match the project’s task scheduling model. By mapping these realistic operational aspects to a **QAOA-based optimization framework**, the project demonstrates both **technical validity** and **real-world relevance**, supporting its potential application in next-generation satellite missions.
The operational characteristics of LEO Earth observation missions described above provide the real-world foundation for the scheduling approaches evaluated in the following sections.


### 3.7 Classical Scheduling Baseline

The classical approach follows a **rule-based heuristic scheduler**, commonly used in traditional mission planning systems. Scheduling decisions are made independently for each visibility window, based on feasibility and priority.

This approach is computationally efficient but inherently **local in nature**, limiting its ability to optimize across multiple windows or future energy requirements.

---

### 3.8 Quantum Scheduling Using QAOA

The quantum approach models the scheduling problem as a **global combinatorial optimization task** and applies the Quantum Approximate Optimization Algorithm (QAOA).

Key characteristics include:
- Binary encoding of task selection
- Cost function combining energy and priority
- Global optimization via quantum superposition
- Probabilistic interpretation of results

The QAOA implementation is executed in a **simulation environment**, consistent with current quantum computing research practices.

---

## 4. Reference to Experimental Results

A detailed comparison of classical and quantum scheduling results, including graphical outputs and probability distributions, has been presented in a separate results and comparison section of this project.

In summary:
- The classical scheduler produces deterministic task selections per visibility window.
- The QAOA-based scheduler outputs probability distributions that reflect global energy–priority trade-offs.

This case study builds upon those results rather than repeating them.

---

## 5. Mission-Level Interpretation of Results

When interpreted within the context of a realistic satellite mission, the previously obtained results reveal several important insights:

- Classical scheduling tends to favor immediate feasibility and priority, even when it leads to higher cumulative energy usage.
- Quantum scheduling evaluates multiple task combinations simultaneously, enabling more balanced decisions.
- Energy-efficient tasks may be selected by the quantum model even when they have lower classical priority, improving long-term mission sustainability.

These characteristics are particularly valuable for autonomous or long-duration missions where manual rescheduling is impractical.

---

## 6. Simulation Scope and Project Implementation

This project is based entirely on **simulation and algorithmic evaluation**.

The following were implemented:
- A classical scheduling algorithm
- A QAOA-based quantum optimization model
- Comparative analysis of outputs

The following were **not** included:
- Real satellite telemetry
- Live orbital propagation
- Execution on physical quantum hardware

This scope aligns with best practices in early-stage quantum optimization research.

---

## 7. Discussion

The case study demonstrates how quantum optimization can complement or outperform classical heuristics in complex scheduling scenarios. While classical methods remain practical for small-scale or time-critical applications, QAOA offers a scalable framework for future missions with increasing task complexity and autonomy requirements.

Importantly, this study shows that quantum advantage can emerge not from faster computation alone, but from **fundamentally different decision-making mechanisms**.

---

## 8. Conclusion

This case study validates the applicability of QAOA-based optimization to satellite task scheduling under realistic operational constraints. By framing the problem within a mission-level context, the study highlights the potential of quantum algorithms to enhance energy efficiency, improve global scheduling decisions, and support next-generation satellite systems.

---

## 9. Future Scope

- Extension to multi-satellite constellations
- Integration with real orbital dynamics models
- Hybrid classical–quantum schedulers
- Execution on NISQ-era quantum processors
- Adaptive scheduling using AI–quantum integration

---

## 10. Assumptions and Limitations

- All results are simulation-based
- Task parameters are simplified representations
- Hardware noise and quantum errors are not modeled
- The study focuses on conceptual validation rather than deployment

---

## Project Information

**Project Title:** QAOA-Based Energy-Efficient Satellite Task Scheduling under Orbital Visibility Constraints  
**Author:** Shreya Sunil Palase (codeQubit)
**Date:** January 4, 2026  
**Affiliation:** Independent reseacher 

---

## References and Useful Links

1. ESA Sentinel-2 Mission Overview: [https://sentinel.esa.int/web/sentinel/missions/sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)  
2. Landsat-8 Earth Observation: [https://landsat.gsfc.nasa.gov/landsat-8/](https://landsat.gsfc.nasa.gov/landsat-8/)  
3. QAOA Algorithm Introduction: [https://quantumcomputing.stackexchange.com/questions/1137/what-is-the-quantum-approximate-optimization-algorithm-qaoa](https://quantumcomputing.stackexchange.com/questions/1137/what-is-the-quantum-approximate-optimization-algorithm-qaoa)  
4. PlanetScope Small Satellite Constellations: [https://www.planet.com/](https://www.planet.com/)  
5. Wikipedia: Low Earth Orbit Satellite [https://en.wikipedia.org/wiki/Low_Earth_orbit](https://en.wikipedia.org/wiki/Low_Earth_orbit)  

**Note:** All task parameters, energy costs, and scheduling results in this project are **simulation-based** and inspired by real-world satellite operations for research purposes.



