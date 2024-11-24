
class Action:
    def __init__(self, name, preconditions, effects, cost=1):
        self.name = name
        self.preconditions = set(preconditions)
        self.effects = set(effects)
        self.cost = cost

    def is_applicable(self, state):
        return self.preconditions.issubset(state)

    def apply(self, state):
        return state | self.effects  

    def __repr__(self):
        return f"{self.name} (Cost: {self.cost})"

# Define the H_FF algorithm
def h_ff(initial_state, goal_state, actions):
    # Relaxed forward simulation
    current_state = initial_state
    relaxed_plan = []  
    action_sets = []  

    while not goal_state.issubset(current_state):
        applicable_actions = [a for a in actions if a.is_applicable(current_state)]
        if not applicable_actions:
            return float('inf')  
        
        action_sets.append(applicable_actions)
        for action in applicable_actions:
            current_state = action.apply(current_state)
            relaxed_plan.append(action)

    
    current_goal = goal_state
    minimal_plan = []
    for applicable_actions in reversed(action_sets):
        required_actions = [
            a for a in applicable_actions if not current_goal.isdisjoint(a.effects)
        ]
        minimal_plan.extend(required_actions)
        for action in required_actions:
            current_goal = current_goal - action.effects | action.preconditions


    heuristic_value = sum(a.cost for a in minimal_plan)
    return heuristic_value

# Example: Relaxed Planning Problem
initial_state = {"at_A"}
goal_state = {"at_C"}
actions = [
    Action("Move A to B", {"at_A"}, {"at_B"}, cost=1),
    Action("Move B to C", {"at_B"}, {"at_C"}, cost=1),
    Action("Move A to C", {"at_A"}, {"at_C"}, cost=2),  # Direct but more costly
]


h_value = h_ff(initial_state, goal_state, actions)
print("Heuristic Value (H_FF):", h_value)
