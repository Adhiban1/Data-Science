import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
os.system('clear')

agent = [0, 0]
wall = [[1, i-1] for i in range(20)]
target = [25,25]
directions = [[1,0],[0,1],[-1,0],[0,-1]]
grid = []
for i in range(-2, 27):
    for j in range(-2, 27):
        grid.append([i,j])

pathx = [agent[0]]
pathy = [agent[1]]
writer = imageio.get_writer('graph.mp4', fps=8)
for i in range(200):
    distances = []
    for direction in directions:
        agent1 = [agent[0]+direction[0], agent[1]+direction[1]]
        if agent1 not in wall:
            distances.append((agent1[0]-target[0])**2+(agent1[1]-target[1])**2)
        else:
            distances.append(10000)
        plt.plot([i[0] for i in grid], [i[1] for i in grid], 'o', markersize=1)
        plt.plot(pathx, pathy, color='gray')
        plt.plot([agent[0]]+[agent1[0], target[0]], [agent[1]]+[agent1[1], target[1]], '--', color='gray')
        plt.plot([i[0] for i in wall], [i[1] for i in wall], color='black')
        plt.plot(agent1[0], agent1[1], 'o', color='black', markersize=3)
        plt.plot(target[0], target[1], 'o', color='green', markersize=10)
        plt.plot(agent[0], agent[1], 'o', color='red')
        plt.ylim(-2, 26)
        plt.xlim(-2, 26)
        plt.axis('off')
        plt.savefig('image.jpg')
        image = imageio.imread('image.jpg')
        writer.append_data(image)
        plt.close()
    if agent == target:
        break
    next_step = directions[np.argmin(distances)]
    agent[0] += next_step[0]
    agent[1] += next_step[1]

    pathx.append(agent[0])
    pathy.append(agent[1])
    print(agent)

writer.close()    