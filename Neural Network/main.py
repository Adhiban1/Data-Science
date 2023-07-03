from NeuralNetwork import NN
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

X = np.random.randn(1000, 3)
Y = np.random.randn(1000, 1)

nn = NN(X, Y, [4, 4], 0) # (X, Y, no.of.hiddenlayers, random_state)
loss_history = nn.back_propagation(0.01, 0.01, 200) # (h, lr, epochs)

plt.plot(loss_history)
plt.title("Loss")
plt.savefig('loss.png')
plt.show()

# h is one parameter, by tuning this parameter we will get good results.