# Step2 - Problem Formulation for Satellite Task Scheduling  
### From Real-World Mission Scenario to Optimization Model

---

## 1. Introduction

After understanding the real-world satellite task scheduling problem, the next step is to **formally define the problem** in a structured and simplified manner.  

Problem formulation acts as a **bridge** between:
- Real satellite operations  
- Mathematical optimization models  
- Quantum algorithms such as QAOA  

In this step, we define a **toy but realistic mission setup** that captures all essential constraints:
- Limited energy
- Visibility windows
- Task priorities
- Task conflicts  

This simplified setup will later be extended to a full-scale optimization and QAOA formulation.

---

## 2. Example Mission Setup

To clearly explain the problem, we consider a **single-satellite mission** operating over a short planning horizon.

### Mission Assumptions
- **Number of satellites:** 1  
- **Number of tasks:** 4  
- **Number of visibility windows:** 3  
- **Energy source:** Battery with limited capacity  
- **Execution model:** Only one task can be executed at a time  

This simplified scenario helps isolate the core scheduling challenges without unnecessary complexity.

---

## 3. Definition of Tasks

Each task represents a real satellite operation such as imaging, sensing, or communication.  
Each task is characterized by:
- Energy cost
- Priority level
- Visibility window constraint

---

## 4. Task Information Table

| Task ID | Task Description                | Energy Cost | Priority Level | Visibility Window |
|-------|---------------------------------|-------------|---------------|------------------|
| T1    | High-resolution Earth imaging   | 2 units     | High          | W1               |
| T2    | Ground data communication       | 1 unit      | Medium        | W1               |
| T3    | Weather sensing operation       | 3 units     | High          | W2               |
| T4    | Scientific experiment           | 3 units     | Low           | W3               |

---

## 5. Detailed Description of Each Task

This section explains **what each task means in a real satellite context**, why it consumes energy, and why its visibility window matters.

---

### 5.1 Task T1: High-Resolution Earth Imaging

**Real-world meaning:**  
This task represents capturing high-resolution images of a specific Earth region, such as a disaster-affected area or a strategic location.

**Why it consumes energy:**  
- High-power imaging sensors  
- Precise attitude control for pointing  
- Data processing and temporary storage  

**Priority rationale:**  
This task has **high priority** because:
- It may support emergency response
- Missed imaging opportunities cannot be recovered

**Visibility window constraint:**  
- Task T1 can only be executed during **Visibility Window W1**, when the target area is within the satellite’s field of view.

---

### 5.2 Task T2: Ground Data Communication

**Real-world meaning:**  
This task involves transmitting collected data to a ground station and receiving operational commands.

**Why it consumes energy:**  
- Communication antennas require transmission power  
- Signal processing and encoding consume onboard resources  

**Priority rationale:**  
Medium priority because:
- Communication is important
- But it may be deferred to a later pass if necessary

**Visibility window constraint:**  
- Task T2 is also limited to **Visibility Window W1**, creating a conflict with Task T1.

---

### 5.3 Task T3: Weather Sensing Operation

**Real-world meaning:**  
This task collects atmospheric data such as temperature and humidity, contributing to weather prediction models.

**Why it consumes energy:**  
- Multiple sensors operate simultaneously  
- Longer sensing duration  

**Priority rationale:**  
High priority because:
- Weather data is time-sensitive
- Delayed sensing reduces forecast accuracy

**Visibility window constraint:**  
- Can only be executed during **Visibility Window W2**, corresponding to a specific orbital region.

---

### 5.4 Task T4: Scientific Experiment

**Real-world meaning:**  
This task represents a scientific payload experiment, such as radiation measurement or microgravity research.

**Why it consumes energy:**  
- Specialized instruments
- Continuous operation for meaningful results

**Priority rationale:**  
Low priority because:
- Scientific experiments are often flexible
- Can be postponed without immediate consequences

**Visibility window constraint:**  
- Executable only during **Visibility Window W3**.

---

## 6. Visibility Windows Explanation

Visibility windows represent **time intervals during which a task is feasible**.

| Window | Description |
|------|------------|
| W1   | Satellite passes over target region and ground station |
| W2   | Satellite flies over weather-sensitive region |
| W3   | Satellite enters region suitable for scientific experiment |

**Important Notes**
- Visibility windows are **non-overlapping in time** in this example
- Tasks assigned to the same window compete for execution
- Tasks cannot be shifted outside their assigned windows

---

## 7. Energy Budget Constraint

The satellite operates on a **limited energy budget**.

### Energy Assumption
- **Total available energy:** 5 units (example value)

### Energy Costs
- T1: 2 units  
- T2: 1 unit  
- T3: 3 units  
- T4: 3 units  

### Key Constraint (Plain English)
> The total energy consumed by all selected tasks must not exceed the available battery energy.

This constraint forces the scheduler to **choose tasks carefully**, especially high-energy ones.

---

## 8. Task Conflicts and Scheduling Challenges

### Conflict Example
- T1 and T2 both require **Visibility Window W1**
- Only one task can be executed in W1
- The scheduler must choose between:
  - High-priority imaging (T1)
  - Medium-priority communication (T2)

### Trade-offs
- Selecting high-priority tasks may consume more energy
- Selecting low-energy tasks may allow more total tasks
- Visibility constraints restrict flexibility

---

## 9. Objective of the Scheduling Problem (Plain English)

The goal of the satellite scheduler is to:

> **Select a subset of tasks that maximizes overall mission value while respecting energy limits and visibility window constraints.**

More specifically:
- Prefer **high-priority tasks**
- Avoid exceeding the energy budget
- Ensure each task is executed only in its allowed visibility window
- Execute at most one task per visibility window

---

## 10. Why This Formulation Is Important for QAOA

This problem naturally maps to:
- **Binary decision variables** (execute or skip a task)
- **Constraint-based optimization**
- **Combinatorial decision-making**

Each task selection becomes a binary variable, making it suitable for:
- QUBO formulation
- Ising Hamiltonian representation
- QAOA-based solution strategies

---

## 11. Summary

This problem formulation:
- Converts real satellite operations into structured components
- Highlights key constraints and trade-offs
- Prepares the foundation for mathematical modeling

This example mission will be used in the next step to:
- Define decision variables
- Write constraints mathematically
- Build a cost function for optimization

---

## Author & Document Information

**Author:** Shreya Sunil Palase(codeQubit)

**Affiliation**:Independent researcher

**Project:** QAOA-Based Energy-Efficient Satellite Task Scheduling  

**Date:** 30 December 2025  

---
