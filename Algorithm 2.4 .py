class Action:
    def __init__(self, name, is_relevant, preconditions, effects):
        self.name = name
        self.is_relevant = is_relevant
        self.preconditions = preconditions
        self.effects = effects

    def __repr__(self):
        return self.name

# Backward-search implementation
def backward_search(initial_state, goal_state, actions):
    plan = []  
    goal = goal_state  
    
    while True:
        
        if initial_state == goal:
            return plan

       
        relevant_actions = [
            action for action in actions if action.is_relevant(goal)
        ]

      
        if not relevant_actions:
            return "Failure: Goal is not achievable"

        
        chosen_action = relevant_actions[0]

       
        goal = chosen_action.preconditions

       
        plan.insert(0, chosen_action)

# Example Usage: Grid Navigation

grid_size = (3, 3)


def is_relevant_to_goal(state, target_effect):
    return state == target_effect

actions = [
    Action(
        "Move Up",
        lambda goal: is_relevant_to_goal(goal, (1, 0)),
        preconditions=(0, 0),
        effects=(1, 0),
    ),
    Action(
        "Move Right",
        lambda goal: is_relevant_to_goal(goal, (1, 1)),
        preconditions=(1, 0),
        effects=(1, 1),
    ),
    Action(
        "Move Down",
        lambda goal: is_relevant_to_goal(goal, (2, 1)),
        preconditions=(1, 1),
        effects=(2, 1),
    ),
    Action(
        "Move Left",
        lambda goal: is_relevant_to_goal(goal, (2, 0)),
        preconditions=(2, 1),
        effects=(2, 0),
    ),
]


initial_state = (0, 0)
goal_state = (2, 0)


result = backward_search(initial_state, goal_state, actions)
print("Plan to achieve the goal:", result)
