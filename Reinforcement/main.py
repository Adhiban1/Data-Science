import matplotlib.pyplot as plt
from rich.progress import track
import imageio
import random
from math import sqrt
import time
import joblib
import numpy as np

a = [0, 0]
destination = [20,10]
u = [0, 1]
d = [0, -1]
l = [-1, 0]
r = [1, 0]

# r2 = 1/sqrt(2)
# d = [[0, 1], [0, -1], [-1, 0], [1, 0], [r2, r2], [-r2, -r2], [r2, -r2], [-r2, r2]]
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
random_choice = random.choice(d)
pre = random_choice
x = [a[0]]
y = [a[1]]
writer = imageio.get_writer('graph0.gif', fps=15)
for s in track(range(100)):
    while True:
        random_choice = random.choice(d)
        if random_choice != [-i for i in pre] and \
        -5 <= a[0]+random_choice[0] <= 5 and -5 <= a[1]+random_choice[1] <= 5:
            pre = random_choice
            break
    
    # c = np.argmin([(a[0]+i[0]-destination[0])**2 + (a[1]+i[1]-destination[1])**2 for i in d])
    # print(c)
    # a[0] += d[c][0]
    # a[1] += d[c][1]
    a[0] += random_choice[0]
    a[1] += random_choice[1]

    x.append(a[0])
    y.append(a[1])
    
    plt.plot(x, y, color='grey')
    if len(x)>5:
        plt.plot(x[-5:], y[-5:], color='red')
    else:
        plt.plot(x, y)
    # plt.plot([a[0], destination[0]], [a[1], destination[1]], '--', color='lightblue')
    plt.plot([destination[0]],[destination[1]], 'o', color='green', markersize=10)
    plt.plot(x[-1], y[-1], 'o', color='red')
    plt.axis('off')
    # plt.xlim(-6, 6)
    # plt.ylim(-6, 6)
    plt.savefig('image.png')
    plt.close()
    image = imageio.imread('image.png')
    writer.append_data(image)
    if a == destination:
        break

writer.close()