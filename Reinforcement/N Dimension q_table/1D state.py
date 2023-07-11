import random

env = [1, 0, 0, 0, 10]
q = [[0, 0] for _ in range(len(env))]
state = 2
for i in range(100):
    action = random.choice([0, 1])
    if state == 0:
        action = 1
    elif state == len(env) - 1:
        action = 0
    move = action if action == 1 else -1
    next_state = state + move
    q[state][action] = env[state] + 0.9 * max(q[next_state][0], q[next_state][1])
    state = next_state
print(f'\r{q} {state}', end='', flush=True)