# 1D state

## Environment:

$env = [e_1, e_2, \dots e_n]$

Example: $env = [1, 0, 0, 0, 10]$. Here 1 and 10 are rewards.

## Q-table:

$q = [[0, 0], [0, 0], \dots n \space terms]$

## Random action:

$action = 0 \space or \space 1$ (left, right)

## Q-table update:

$reward = env(state)$

$alpha = 0.9$

$Q(state,action) = reward + alpha \times max(Q(next\_state, actions))$

# 2D state

## Environment:

$$
\begin{bmatrix}
e_{11} & e_{12} & \dots & e_{1n} \\
e_{21} & e_{22} & \dots & e_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
e_{m1} & e_{m2} & \dots & e_{mn} \\
\end{bmatrix}
$$

Example: 

```python
env = [
    [0, -1,  0, 0],
    [0, -1,  0, 0],
    [0,  0, 10, 0],
    [0,  0,  0, 0]
]
```

Here 10 is reward and -1 is penality.

## Q-table:

$$
\begin{bmatrix}
[0,0,0,0] & [0,0,0,0] & \dots & n \space terms \\
[0,0,0,0] & [0,0,0,0] & \dots & [0,0,0,0] \\
\vdots & \vdots & \ddots & \vdots \\
m \space terms & [0,0,0,0] & \dots & [0,0,0,0] \\
\end{bmatrix}
$$

```python
q = [[[0 for _ in range(4)] for _ in range(len(env[0]))] for _ in range(len(env))]
```

## Random action:

$action = 0 \space or \space 1 \space or \space 2 \space or \space 3$ (up, down, left, right)

## Q-table update:

$reward = env(next\_state)$

$alpha = 0.9$

$$Q(state,action) = reward + alpha * max(Q(next\_state,actions))$$