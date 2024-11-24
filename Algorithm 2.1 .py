#Direct implementation of the Algorithm

import random

def forward_search(initial_state, goal_state, actions, transition_function, goal_test):
    """
    Forward search algorithm implementation.
    
    Parameters:
        initial_state (any): The starting state (s₀).
        goal_state (any): The desired goal state (g).
        actions (list): A list of available actions (A).
        transition_function (function): A function γ(s, a) to get the next state.
        goal_test (function): A function to check if a state satisfies the goal.
    """
    
    state = initial_state 
    plan = []              
    
    while True:
        
        if goal_test(state, goal_state):
            return plan  
        
        
        applicable_actions = [action for action in actions if action.is_applicable(state)]
        
        
        if not applicable_actions:
            return "failure"
        
        # Nondeterministic approach
        chosen_action = random.choice(applicable_actions)
        
        
        state = transition_function(state, chosen_action)
        
       
        plan.append(chosen_action)
  

# Now assuming the actor to be a robot on a 3x3 grid  
  

class Action:
    def __init__(self, name, is_applicable, transition):
        self.name = name
        self.is_applicable = is_applicable
        self.transition = transition

    def __repr__(self):
        return self.name


grid_size = (3, 3)


def move_up(state):
    x, y = state
    return (x - 1, y) if x > 0 else None

def move_down(state):
    x, y = state
    return (x + 1, y) if x < grid_size[0] - 1 else None

def move_left(state):
    x, y = state
    return (x, y - 1) if y > 0 else None

def move_right(state):
    x, y = state
    return (x, y + 1) if y < grid_size[1] - 1 else None

ACTIONS = [
    Action("Move Up", lambda s: move_up(s) is not None, move_up),
    Action("Move Down", lambda s: move_down(s) is not None, move_down),
    Action("Move Left", lambda s: move_left(s) is not None, move_left),
    Action("Move Right", lambda s: move_right(s) is not None, move_right),
]


def transition_function(state, action):
    return action.transition(state)

def goal_test(state, goal_state):
    return state == goal_state


initial_state = (0, 0)
goal_state = (2, 2)
result = forward_search(initial_state, goal_state, ACTIONS, transition_function, goal_test)
print("Plan:", result)
