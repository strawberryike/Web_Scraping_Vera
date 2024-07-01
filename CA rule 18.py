# Rule 18 {0, 0, 0, 1, 0, 0, 1, 0}
# 111, 110, 101, 100, 011, 010, 001, 000

# import numpy as np
# import cellpylib as cpl

# cellular_automaton = np.array([[0, 0, 0, 1, 0, 0, 1, 0]])

# cellular_automaton = cpl.evolve(cellular_automaton, timesteps=5, memoize=True, 
# apply_rule=lambda n, c, t: cpl.nks_rule(n, rule:18)) 

import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, state, pos):
    left, center, right = state[pos - 1], state[pos], state[(pos + 1) % len(state)]
    return rule[left * 4 + center * 2 + right]

def evolve(rule, initial_state, steps):
    state, history = initial_state.copy(), [initial_state.copy()]
    for _ in range(steps):
        state = np.array([apply_rule(rule, state, i) for i in range(len(state))])
        history.append(state.copy())
    return history

def plot_evolution(history):
    plt.figure(figsize=(10, 5))
    plt.imshow(history, cmap="binary", interpolation="nearest")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Rule 18 Cellular Automaton Evolution")
    plt.show()

rule18 = np.array([0, 0, 0, 1, 1, 0, 0, 1], dtype=int)
initial_state = np.zeros(101, dtype=int)
initial_state[50] = 1

steps = 100
evolution_history = evolve(rule18, initial_state, steps)
plot_evolution(np.array(evolution_history))

