import random
import matplotlib.pyplot as plt
import numpy as np
import imageio.v2 as imageio

class Agent:
    def __init__(self, r, c, init_state, alpha, beta, *rewards):
        self.r = r
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.q_table = [[0]*c for _ in range(r)]
        self.rewards = [[0]*c for _ in range(r)]

        for l in rewards:
            self.rewards[l[0]][l[1]] = l[2]
        self.state = init_state
    
    def move(self):
        s = self.state
        a = random.choice([
            [1, 0], [0, 1],
            [-1, 0], [0, -1]
        ])
        s = [s[0]+a[0], s[1]+a[1]]
        
        if s[0] < 0:
            s[0] = 1
        elif s[0] > self.r - 1:
            s[0] = self.r - 2
        if s[1] < 0:
            s[1] = 1
        elif s[1] > self.c - 1:
            s[1] = self.c - 2
        
        self.state = s
        self.update_table()
    
    def update_table(self):
        s = self.state
        
        if s == [0, 0]:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[1][0] - self.alpha,
                    self.q_table[0][1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s == [0, self.c-1]:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[1][self.c-1] - self.alpha,
                    self.q_table[0][self.c-2] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s == [self.r-1, 0]:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[self.r-1][1] - self.alpha,
                    self.q_table[self.r-2][0] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s == [self.r-1, self.c-1]:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[self.r-1][self.c-2] - self.alpha,
                    self.q_table[self.r-2][self.c-1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s[0] == 0:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[s[0]+1][s[1]] - self.alpha,
                    self.q_table[s[0]][s[1]+1] - self.alpha,
                    self.q_table[s[0]][s[1]-1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s[0] == self.r - 1:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[s[0]-1][s[1]] - self.alpha,
                    self.q_table[s[0]][s[1]+1] - self.alpha,
                    self.q_table[s[0]][s[1]-1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s[1] == 0:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[s[0]+1][s[1]] - self.alpha,
                    self.q_table[s[0]-1][s[1]] - self.alpha,
                    self.q_table[s[0]][s[1]+1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        elif s[1] == self.c - 1:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[s[0]+1][s[1]] - self.alpha,
                    self.q_table[s[0]-1][s[1]] - self.alpha,
                    self.q_table[s[0]][s[1]-1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]
                
        
        else:
            if self.rewards[s[0]][s[1]] == 0:
                self.q_table[s[0]][s[1]] = max(
                    self.q_table[s[0]+1][s[1]] - self.alpha,
                    self.q_table[s[0]-1][s[1]] - self.alpha,
                    self.q_table[s[0]][s[1]+1] - self.alpha,
                    self.q_table[s[0]][s[1]-1] - self.alpha
                ) * self.beta
            else:
                self.q_table[s[0]][s[1]] = self.rewards[s[0]][s[1]]

def image_save(agent):
    plt.imshow(np.array(agent.q_table).T, cmap='gray')
    plt.clim(np.array(agent.q_table).min(), np.array(agent.q_table).max())
    plt.xlim(-0.5, agent.r - 0.5)
    plt.ylim(-0.5, agent.c - 0.5)
    plt.title(f'Q- Table')
    plt.savefig('image.jpg')
    plt.close()
       
def RL():
    agent = Agent(20, 20, [0, 5], 1, 0.9, 
                (5,5,10), (5,4,-1), (5,7,-1), 
                (4,5,-1), (15,15,10))

    n = 100000
    segment = 60*10
    video = False
    
    if segment > n:
        segment = n
    
    if video:
        writer = imageio.get_writer('video.mp4', fps=60)
    
    for i in range(n):
        agent.move()
        if ((i+1) % (n//segment) == 0 or i+1 == n) and video:
            image_save(agent)
            image = imageio.imread('image.jpg')
            writer.append_data(image)
        print(f'\r{(i+1)*100/n:.2f}%', end='')
        
    if video:
        writer.close()
    else:
        image_save(agent)

RL()