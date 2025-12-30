# Understanding the Real Satellite Task Scheduling Problem  
### Foundation for QAOA-Based Energy-Efficient Optimization

---

## 1. Introduction

Satellite missions are no longer limited to a single objective. Modern satellites are expected to perform **multiple tasks simultaneously**, such as Earth imaging, weather monitoring, scientific experiments, and communication with ground stations.

However, satellites operate in an **extremely constrained environment**:
- They have **limited onboard energy**
- They follow **fixed orbital paths**
- They can interact with Earth **only during short visibility windows**
- They must operate autonomously with minimal human intervention

Satellite task scheduling is the decision-making process that determines **what the satellite should do, when it should do it, and how resources are allocated**. Understanding this real-world problem is essential before translating it into an optimization model suitable for **Quantum Approximate Optimization Algorithm (QAOA)**.

---

## 2. What Is Satellite Task Scheduling?

Satellite task scheduling refers to the process of **selecting, sequencing, and timing satellite tasks** over a given planning horizon while respecting physical and operational constraints.

In simple terms, it answers the question:

> *Given many possible tasks and very limited resources, which tasks should the satellite perform to maximize mission value?*

---

### 2.1 Key Components of the Scheduling Problem

A real satellite scheduling problem consists of:

- **Tasks:** Activities the satellite can perform  
- **Resources:** Energy, time, communication bandwidth  
- **Constraints:** Visibility windows, battery limits, task conflicts  
- **Objectives:** Mission goals such as maximizing coverage or data return  

Each scheduling decision has **long-term consequences**, especially for energy usage and mission lifespan.

---

## 3. Why Satellite Task Scheduling Is Important

Satellite scheduling directly impacts **mission success, efficiency, and longevity**.

---

### 3.1 Autonomous Operation Requirement

Satellites orbit Earth multiple times per day and cannot rely on continuous ground control. Therefore:
- Scheduling decisions must be made **automatically**
- Plans must be robust to uncertainty
- Real-time re-scheduling is often required

---

### 3.2 Limited and Non-Recoverable Resources

Unlike terrestrial systems:
- Energy cannot be replenished on demand
- Hardware failures cannot be repaired easily
- Missed tasks cannot be recovered later

This makes optimal resource utilization **critical**.

---

### 3.3 High Cost of Satellite Missions

Launching and operating satellites costs **millions to billions of dollars**. Poor scheduling:
- Wastes expensive mission time
- Reduces scientific and commercial return
- Shortens mission lifetime

---

## 4. Real Satellite Tasks: What Does a Satellite Actually Do?

A satellite typically performs **multiple categories of tasks**, each with different requirements and constraints.

---

### 4.1 Earth Observation / Imaging Tasks

**What it is:**  
The satellite captures images of Earth’s surface using optical or radar sensors.

**Why it matters:**  
Earth observation supports:
- Disaster monitoring (floods, fires)
- Agriculture planning
- Urban development
- National security

**Key Constraints Explained**
- **Visibility:** Target must be within the satellite’s field of view
- **Energy:** Cameras and stabilization systems consume high power
- **Time:** Imaging must occur within a short orbital pass
- **Data storage:** Images generate large volumes of data

**Example:**  
A satellite may have only **90 seconds** to image a specific city during one orbit.

---

### 4.2 Weather and Environmental Sensing

**What it is:**  
Sensors measure atmospheric and environmental parameters.

**Why it matters:**  
Accurate weather prediction and climate monitoring depend on frequent satellite measurements.

**Key Constraints**
- Often **periodic** tasks
- Moderate energy consumption
- Time-sensitive for forecasting accuracy

**Example:**  
Collecting temperature and humidity profiles every orbit over ocean regions.

---

### 4.3 Ground Communication Tasks

**What it is:**  
Sending collected data to Earth and receiving commands.

**Why it matters:**  
Without communication, collected data is useless.

**Key Constraints**
- Requires line-of-sight to ground stations
- Limited communication windows
- High transmission energy cost
- Competes with observation tasks

**Example:**  
A satellite may see a ground station for only **5–10 minutes per orbit**.

---

### 4.4 Scientific Experiment Tasks

**What it is:**  
Experiments studying space physics, radiation, or microgravity.

**Why it matters:**  
Advances scientific understanding and space technology.

**Key Constraints**
- May require specific orbital regions
- Can be long-duration
- Often flexible but energy-intensive

---

## 5. Core Real-World Constraints in Satellite Scheduling

Understanding constraints is essential because **they define the optimization problem structure**.

---

### 5.1 Limited Battery and Energy Budget

Satellites rely on:
- Solar panels (generation)
- Batteries (storage)

**Why energy is limited**
- Solar exposure varies across orbit
- Battery capacity is finite
- Batteries degrade over time

**Energy-consuming subsystems**
- Payload instruments
- Communication antennas
- Attitude control systems
- Onboard processors

**Constraint Meaning**
> At any time, total energy consumption must not exceed available battery energy.

---

### 5.2 Orbital Visibility Windows

Satellites move at high speed (~7.5 km/s in LEO).

**Visibility window means**
- A task can only be executed when the satellite is geometrically aligned with its target

**Types of visibility**
- Target visibility (imaging)
- Ground station visibility (communication)
- Sunlight visibility (charging)

**Why this is challenging**
- Windows are short
- Shift over time
- Often overlap

---

### 5.3 Time Window Overlap

Multiple tasks may be feasible at the same time.

**Problem**
- Satellite usually executes **only one task at a time**
- Overlapping windows create conflicts

**Result**
- Scheduler must choose **which task to execute and which to skip**

This is a key source of **combinatorial complexity**.

---

### 5.4 Task Priority and Mission Objectives

Not all tasks have equal importance.

**Priority factors**
- Emergency response
- Commercial value
- Scientific significance
- Deadline constraints

**Example**
- Disaster imaging has higher priority than routine mapping

Scheduling must balance **priority vs resource usage**.

---

### 5.5 Task Execution Duration

Each task has:
- Fixed execution time
- Setup and switching overhead

**Constraint**
> A task must fully fit inside its visibility window without interruption.

Partial execution is often **not allowed**.

---

## 6. Why Optimization Is Needed

Satellite scheduling is:
- NP-hard
- High-dimensional
- Constraint-heavy

**Why simple rules fail**
- Greedy approaches ignore long-term impact
- Manual planning does not scale
- Heuristics may miss optimal solutions

Optimization allows **global reasoning** over all tasks and constraints.

---

## 7. Why Advanced Optimization and Quantum Methods?

As satellite constellations grow:
- Task count increases exponentially
- Classical solvers struggle with real-time planning

**Why QAOA is promising**
- Naturally models binary decision variables
- Handles combinatorial structure efficiently
- Suitable for hybrid quantum–classical systems
- Potential advantage for large-scale scheduling

---

## 8. Real-World Applications

### Space Agencies
- **NASA:** Earth observation, deep space missions
- **ISRO:** Remote sensing and navigation
- **ESA:** Scientific and commercial satellites

### Commercial Companies
- **SpaceX:** Communication scheduling (Starlink)
- **Planet Labs:** High-frequency Earth imaging
- **Maxar:** High-resolution mapping

### Defense and Security
- Surveillance
- Secure communications
- Reconnaissance missions

---

## 9. Research Questions and Explanations

### Why is satellite task scheduling difficult?
Because it combines limited resources, strict timing constraints, and competing objectives into a combinatorial optimization problem.

---

### Why is energy efficiency a primary objective?
Energy directly determines how long the satellite can operate and how many tasks it can complete.

---

### Why are visibility constraints unavoidable?
They are dictated by orbital mechanics and cannot be bypassed through software.

---

### Why is optimization superior to rule-based scheduling?
Optimization considers long-term trade-offs and global resource allocation.

---

## 10. Summary and Transition to Next Step

This document establishes a **realistic understanding** of satellite task scheduling, highlighting:
- Task diversity
- Energy limitations
- Visibility constraints
- Priority-driven decision-making

These characteristics directly motivate:
- Binary decision variables
- Constraint-based optimization models
- QUBO / Ising formulations for QAOA

---
---

## Author & Document Information

**Author:** Shreya Sunil Palase

**Affiliation:** (Independent Researcher)  

**Project:** QAOA-Based Energy-Efficient Satellite Task Scheduling  

**Date:** 30 December 2025  

---
