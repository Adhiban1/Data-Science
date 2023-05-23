import random
import imageio
import matplotlib.pyplot as plt
from rich.progress import track

random.seed(1)

class RL:
    def __init__(self):
        self.q_table = [1]*10
        self.actions = [1, -1]
        self.state = 2
    
    def update_qtable(self, state, nextState):
        if nextState == 0:
            self.q_table[nextState] = 10
        elif nextState == 5:
            self.q_table[nextState] = 20
        elif nextState == 7:
            self.q_table[nextState] = 5
        elif nextState == 9:
            self.q_table[nextState] = 50
        else:
            if self.q_table[state] > self.q_table[nextState]:
                self.q_table[nextState] = self.q_table[state] * 0.8
        self.state = nextState
    
    def nextState(self, explore):
        if self.state == 0:
            next_state = 1
        elif self.state == 9:
            next_state = 8
        else:
            if random.random() < explore:
                next_state = self.state + random.choice(self.actions)
            else:
                if self.q_table[self.state + 1] > self.q_table[self.state - 1]:
                    next_state = self.state + 1
                else:
                    next_state = self.state - 1
        return next_state

rl = RL()
writer = imageio.get_writer('video.mp4', fps=5)

for i in track(range(100)):
    rl.update_qtable(rl.state, rl.nextState(1))

    plt.plot(rl.q_table, '--', color='black')
    plt.plot([0, 5, 7, 9], [rl.q_table[0], rl.q_table[5], rl.q_table[7], rl.q_table[9]], 'ro', label='Reward')
    plt.plot(rl.state, rl.q_table[rl.state], 'o', color='blue', label='Agent')
    plt.text(0, rl.q_table[0], s='10')
    plt.text(5, rl.q_table[5], s='20')
    plt.text(7, rl.q_table[7], s='5')
    plt.text(9, rl.q_table[9], s='50')
    plt.legend()
    plt.axis('off')

    plt.title(f'Loop: {i+1}')
    plt.savefig('graph.jpg')
    plt.close()

    img = imageio.imread('graph.jpg')
    writer.append_data(img)

writer.close()
