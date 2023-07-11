import random

env = [
    [0, -1,  0, 0],
    [0, -1,  0, 0],
    [0,  0, 10, 0],
    [0,  0,  0, 0]
]
q = [[[0 for _ in range(4)] for _ in range(len(env[0]))] for _ in range(len(env))]

state = [0, 0]
for i in range(1000):
    action = random.choice([
        [-1,0],[1,0],[0,-1],[0,1]
    ])

    next_state = [state[0] + action[0], state[1] + action[1]]

    if next_state[0] > len(env) - 1:
        next_state[0] -= 2
        action = [-1, 0]
    elif next_state[0] < 0:
        next_state[0] += 2
        action = [1, 0]
    if next_state[1] > len(env[0]) - 1:
        next_state[1] -= 2
        action = [0, -1]
    elif next_state[1] < 0:
        next_state[1] += 2
        action = [0, 1]

    if action == [-1,0]:
        action = 0
    elif action == [1,0]:
        action = 1
    elif action == [0,-1]:
        action = 2
    elif action == [0,1]:
        action = 3

    if env[state[0]][state[1]] != 0:
        q[state[0]][state[1]][0] = env[state[0]][state[1]]
        q[state[0]][state[1]][1] = env[state[0]][state[1]]
        q[state[0]][state[1]][2] = env[state[0]][state[1]]
        q[state[0]][state[1]][3] = env[state[0]][state[1]]
    else:
        q[state[0]][state[1]][action] = env[next_state[0]][next_state[1]] + 0.9 * max(q[next_state[0]][next_state[1]][0], q[next_state[0]][next_state[1]][1], 
                                                                        q[next_state[0]][next_state[1]][2], q[next_state[0]][next_state[1]][3])
    state = next_state

for i in q:
    print([[round(k,3) for k in j] for j in i])