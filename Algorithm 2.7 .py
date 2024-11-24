def lookahead(sigma, current_state, goal):
    """
    Generates a plan from the current state to the goal.
    """
    if current_state == goal:
        return []  # No actions needed if already at the goal
    
    # Define possible transitions based on current state
    transitions = sigma.get("transitions", {})
    if current_state in transitions:
        # Return a plan consisting of a single valid action
        next_action = transitions[current_state]
        return [next_action]
    else:
        return "failure"
def simulate(sigma, current_state, goal, plan):
    """
    Simulates the execution of the given plan to check feasibility.
    Returns 'failure' if the plan cannot be executed as intended.
    """
    simulated_state = current_state
    for action in plan:
        simulated_state = sigma["effects"].get(action, simulated_state)
        if simulated_state == "failure":
            return "failure"
    return simulated_state

# Define the Run-Lazy-Lookahead algorithm
def run_lazy_lookahead(sigma, goal):
    """
    Executes the Run-Lazy-Lookahead algorithm to achieve the goal.
    """
    
    current_state = "room A"  
    print(f"Initial state: {current_state}, Goal: {goal}")
    
    while current_state != goal:
  
        plan = lookahead(sigma, current_state, goal)
        
        
        if plan == "failure":
            print("No valid plan found. Terminating with failure.")
            return "failure"
        
        # Execute the plan lazily
        while plan and current_state != goal and simulate(sigma, current_state, goal, plan) != "failure":
            action = plan.pop(0)  
            print(f"Performing action: {action}")
            
            
            current_state = sigma["effects"].get(action, current_state)
            print(f"Current state: {current_state}")
    
    print("Goal achieved!")
    return "success"


sigma = {
    "actions": ["move_to_B", "move_to_C"],
    "transitions": {
        "room A": "move_to_B",  # In room A, the next action is to move to room B
        "room B": "move_to_C"   # In room B, the next action is to move to room C
    },
    "effects": {
        "move_to_B": "room B",  # Action "move_to_B" results in state "room B"
        "move_to_C": "room C"   # Action "move_to_C" results in state "room C"
    }
}


goal = "room C"
run_lazy_lookahead(sigma, goal)
