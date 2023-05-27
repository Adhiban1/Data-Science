import random
import matplotlib.pyplot as plt
import numpy as np
import imageio
from rich.progress import track


def xyLim(ax):
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)


class AgentPath:
    def __init__(self, agent):
        self.agent = agent
        self.x = []
        self.y = []
        self.add()

    def add(self):
        s = self.agent.state
        self.x.append(s[0])
        self.y.append(s[1])

    def plot(self, ax):
        ax.plot(self.x, self.y, color="grey")
        if len(self.x) > 3:
            ax.plot(self.x[-3:], self.y[-3:], color="red")
        else:
            ax.plot(self.x[-3:], self.y[-3:], color="red")


def addList(a, b):
    return [i + j for i, j in zip(a, b)]


class Agent:
    def __init__(self, target):
        self.state = [random.randint(0, 9) for _ in range(2)]
        self.q_table = [[0] * 10 for _ in range(10)]
        self.target = target

    def plot(self, ax):
        s = self.state
        ax.plot(s[0], s[1], "ro")

    def nextState(self):
        action = random.choice([[1, 0], [0, 1], [-1, 0], [0, -1]])
        s = self.state
        next_state = addList(s, action)

        if next_state[0] > 9:
            next_state[0] -= 2
        if next_state[1] > 9:
            next_state[1] -= 2
        if next_state[0] < 0:
            next_state[0] += 2
        if next_state[1] < 0:
            next_state[1] += 2

        return next_state

    def update(self):
        s = self.state
        ns = self.nextState()

        if ns == self.target.state:
            self.q_table[ns[0]][ns[1]] = 10
        else:
            if self.q_table[ns[0]][ns[1]] < self.q_table[s[0]][s[1]]:
                self.q_table[ns[0]][ns[1]] = self.q_table[s[0]][s[1]] * 0.9
        self.state = ns

    def rand_move(self):
        self.state = self.nextState()


class Target:
    def __init__(self):
        self.state = [5, 7]

    def plot(self, ax):
        s = self.state
        ax.plot(s[0], s[1], "go")


target = Target()
agent = Agent(target)
path = AgentPath(agent)


def print_q_table():
    for i in agent.q_table:
        for j in i:
            print(f"{j:.2f}", end=" | ")
        print()


writer = imageio.get_writer("q_table_video.mp4", fps=60)
for _ in track(range(2000)):
    agent.update()
    path.add()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    path.plot(ax1)
    target.plot(ax1)
    agent.plot(ax1)
    xyLim(ax1)

    im = ax2.imshow(np.array(agent.q_table).T, cmap="gray")
    ax2.set_ylim(-1, 10)
    ax2.set_xlim(-1, 10)
    im.set_clim(0, 10)
    plt.savefig("image2.jpg")
    plt.close()
    image = imageio.imread("image2.jpg")
    writer.append_data(image)

writer.close()
