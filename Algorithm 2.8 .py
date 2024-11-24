import threading
import time
from queue import Queue
def lookahead(sigma, current_state, goal, plan_queue):
    """
    Generates a plan and updates it continuously.
    """
    while True:
        if current_state != goal:
            if current_state in sigma["transitions"]:
                plan = [sigma["transitions"][current_state]]
                plan_queue.put(plan) 
            else:
                plan_queue.put("failure")  
        time.sleep(1) 

# Define the Run-Concurrent-Lookahead algorithm
def run_concurrent_lookahead(sigma, goal):
    """
    Executes the Run-Concurrent-Lookahead algorithm.
    """
    current_state = "room A"  # Starting position of the robot
    plan_queue = Queue()  
    plan_queue.put([]) 
    
    def thread1_lookahead():
        lookahead(sigma, current_state, goal, plan_queue)

    def thread2_execution():
        nonlocal current_state
        while True:
            plan = plan_queue.get()  # Get the latest plan
            if current_state == goal:
                print("Goal achieved!")
                return "success"
            elif plan == "failure":
                print("No valid plan found. Terminating with failure.")
                return "failure"
            elif plan:
                while plan and current_state != goal:
                    action = plan.pop(0)  
                    print(f"Performing action: {action}")
                    current_state = sigma["effects"].get(action, current_state)
                    print(f"Current state: {current_state}")
                    time.sleep(0.5)  # Simulate action execution time

    # Create and start the threads
    thread1 = threading.Thread(target=thread1_lookahead)
    thread2 = threading.Thread(target=thread2_execution)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


sigma = {
    "actions": ["move_to_B", "move_to_C"],
    "transitions": {
        "room A": "move_to_B", 
        "room B": "move_to_C"  
    },
    "effects": {
        "move_to_B": "room B",  
        "move_to_C": "room C"   
    }
}

goal = "room C"
run_concurrent_lookahead(sigma, goal)
