from collections import deque

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

# Deterministic Search Algorithm implementation
def deterministic_search(initial_state, goal_state, actions):
    frontier = deque([([], initial_state)])  
    expanded = set()  

    while frontier:
        
        plan, state = frontier.popleft()

        
        expanded.add(state)

        
        if state == goal_state:
            return plan

        # Generate children nodes
        children = []
        for action in actions:
            if action.is_applicable(state):  
                next_state = action.transition(state)
                if next_state and next_state not in expanded: 
                    new_plan = plan + [action.name]
                    children.append((new_plan, next_state))

        
        frontier.extend(children)

    return "Failure: No solution found"

# Example Usage
initial_state = (0, 0)  
goal_state = (2, 2)  


result = deterministic_search(initial_state, goal_state, ACTIONS)
print("Plan to reach the goal:", result)
