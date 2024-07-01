import numpy as np
import matplotlib.pyplot as plt

results = []

def rule1(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 1, 1
index = rule1(left, center, right)
results.append({"Rule": "Rule 1", "Resulting index": index})

def rule2(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 1, 0
index = rule2(left, center, right)
results.append({"Rule": "Rule 2", "Resulting index": index})

def rule3(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 0, 1
index = rule3(left, center, right)
results.append({"Rule": "Rule 3", "Resulting index": index})

def rule4(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 0, 0
index = rule4(left, center, right)
results.append({"Rule": "Rule 4", "Resulting index": index})

def rule5(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 1, 1
index = rule5(left, center, right)
results.append({"Rule": "Rule 5", "Resulting index": index})

def rule6(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 1, 0
index = rule6(left, center, right)
results.append({"Rule": "Rule 6", "Resulting index": index})

def rule7(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << (center * 2 + left * 4 + right))) else 0
left, center, right = 0, 0, 1
index = rule7(left, center, right)
results.append({"Rule": "Rule 7", "Resulting index": index})

def rule8(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 0 if index & (1 << (center * 2 + left * 4 + right)) else 1
left, center, right = 0, 0, 0
index = rule8(left, center, right)
results.append({"Rule": "Rule 8", "Resulting index": index})

def apply_rules(left, center, right, rule):
    if rule == 1:
        return rule1(left, center, right)
    elif rule == 2:
        return rule2(left, center, right)
    elif rule == 3:
        return rule3(left, center, right)
    elif rule == 4:
        return rule4(left, center, right)
    elif rule == 5:
        return rule5(left, center, right)
    elif rule == 6:
        return rule6(left, center, right)
    elif rule == 7:
        return rule7(left, center, right)
    elif rule == 8:
        return rule8(left, center, right)
    else:
        return 0 

def print_cellular_automaton(initial_state, num_steps, rule):
    current_state = initial_state[:]
    states = [current_state]
    
    for _ in range(num_steps):
        next_state = []
        for i in range(len(current_state)):
            left = current_state[i - 1]
            center = current_state[i]
            right = current_state[(i + 1) % len(current_state)]
            next_value = apply_rules(left, center, right, rule)
            next_state.append(next_value)
        states.append(next_state)
        current_state = next_state
    
    for step, state in enumerate(states):
        print(f"Step {step}: {''.join(map(str, state))}")

initial_state = [0] * 31
initial_state[15] = 1

chosen_rule = 18

num_steps = 50

print_cellular_automaton(initial_state, num_steps, chosen_rule)

