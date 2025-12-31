""" Classical Satellite Task Schedular
-------------------------------------------------------------------------------------
Goal : Find the optimal classical schedule fo satellite tasks under:
- Energy Budget constraint
- Task Priority
- Visibility Constraint
"""
import numpy as np
import itertools
#----------------------------------------------------------------------------------------------
# Define Tasks (from problem_formulator.md Day1 folder file)
# columns : [energy_cost,priority_number,visibility_window]
# Priority Mapping : high=3,medium =2,low=1
#-----------------------------------------------------------------------------------------------

energy=np.array([2,1,3,3])
priority=np.array([3,2,3,1])
windows=np.array(['W1','W1','W2','W3'])

ENERGY_BUDGET=5 # Maximum energy units allow per window

#----------------------------------------------------------------------------------------------
# Cost Function
#---------------------------------------------------------------------------------------------
def compute_cost(selection,energy,priority,windows ,energy_budget=5,current_window='W1'):
    """
    compute the costof given schedule  selection vector.
    Panalize schedules exceeding energy budget or not visible in the current window.
    """
    total_energy=0
    total_priority=0
    for i, x  in enumerate(selection):
        if i>= len(energy) or i>=len(priority) or i>=len(windows):
            raise IndexError(f"Index{i} out of range!")
        if x==1:
            # Check if task is visible current window
            if windows[i]!= current_window:
                return float('inf')  # Invalied if not visible
            total_energy += energy[i]
            total_priority += priority[i]
            # Check Energy Budget
            if total_energy > energy_budget:
                return float('inf') # Invalid id exceed the budget
    return  -total_priority

#-----------------------------------------------------------------------------------------------------------
# Brute Force Scheduler
#-----------------------------------------------------------------------------------------------------------
def find_optimal_schedule(energy,priority,windows,current_window='W1'):
    num_tasks=len(energy)
    best_cost=float('inf')
    best_solution = None

    # Generate all possible  0/1  combination for tasks
    for selection in itertools.product([0,1],repeat=num_tasks):
        cost=compute_cost(selection,energy,priority,windows,current_window=current_window)
        if cost < best_cost:
            best_cost=cost
            best_solution= selection

    if best_solution is None:
            best_solution=tuple([0]*num_tasks)
            best_cost=float('inf')

    return best_solution,best_cost
#-----------------------------------------------------------------------------------------------------------
# Run Sheduler for each window
#-----------------------------------------------------------------------------------------------------------
window = ['W1','W2','W3']
for w in window:
    solution, cost = find_optimal_schedule(energy,priority,windows,current_window=w)
    #print("solution type:", type(solution))
    #print("solution length:", len(solution))
    #print("energy length type:", len(energy))
    selected=np.array(solution,dtype=int)
    print(f"\n Window {w}: Solution={solution},Cost={cost}")
    for i ,s in enumerate(solution):
        if i >= len(energy):
            print(f"Skipping index{i}")
            continue
        if s==1:
            print(f"Task T{i+1}:Energy={energy[i]},Priority={priority[i]}")
    
    