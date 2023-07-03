import numpy as np
from tqdm import tqdm

class NN:
    def __init__(self, X, Y, hidden_layers, randstate=None):
        if randstate:
            np.random.seed(randstate)
        self.X = X
        self.Y = Y
        self.hidden_layers = hidden_layers
        self.layers = [X.shape[1]] + hidden_layers + [Y.shape[1]]
        self.W = self.weights(self.layers)
        self.B = self.bias(self.layers)

    def weights(self, neurons):
        W = []
        for i in range(len(neurons) - 1):
            W.append(np.random.randn(neurons[i], neurons[i + 1]))
        return W

    def bias(self, neurons):
        B = []
        for i in range(1, len(neurons)):
            B.append(np.random.randn(neurons[i]))
        return B

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return (x + abs(x)) / 2

    def forward(self, X, W, B, activation=False):
        for i in range(len(W)):
            if activation:
                if i == len(W) - 1:
                    X = self.sigmoid(X @ W[i] + B[i])
                else:
                    X = self.relu(X @ W[i] + B[i])
            else:
                X = X @ W[i] + B[i]
        return X

    def modify_forward(self, X, W, B, h, hn, hi, hj=0, w_or_b="w", activation=False):
        if w_or_b == "w":
            W[hn][hi][hj] += h
        else:
            B[hn][hi] += h
        for i in range(len(W)):
            if activation:
                if i == len(W) - 1:
                    X = self.sigmoid(X @ W[i] + B[i])
                else:
                    X = self.relu(X @ W[i] + B[i])
            else:
                X = X @ W[i] + B[i]
        return X

    def MSE(self, Yt, Y):
        return ((Yt - Y) ** 2).mean()

    def grad(self, Y, X, W, B, h, lr, activation=False):
        # Weights
        for wt in range(len(W)):
            for wti in range(W[wt].shape[0]):
                for wtj in range(W[wt].shape[1]):
                    f1 = self.modify_forward(X, W, B, h, wt, wti, wtj, activation=activation)
                    f2 = self.modify_forward(X, W, B, -h, wt, wti, wtj, activation=activation)
                    gradient = (self.MSE(Y, f1) - self.MSE(Y, f2)) / (2 * h)
                    W[wt][wti][wtj] -= lr * gradient
        # Bias
        for b in range(len(B)):
            for bi in range(B[b].shape[0]):
                f1 = self.modify_forward(X, W, B, h, b, bi, w_or_b="b", activation=activation)
                f2 = self.modify_forward(X, W, B, -h, b, bi, w_or_b="b", activation=activation)
                gradient = (self.MSE(Y, f1) - self.MSE(Y, f2)) / (2 * h)
                B[b][bi] -= lr * gradient
        return W, B

    def backpropagation(self, h, lr, epochs, activation=False):
        self.activation = True
        loss_history = []
        loss_history.append(self.MSE(self.Y, self.forward(self.X, self.W, self.B, activation)))
        for _ in tqdm(range(epochs)):
            self.W, self.B = self.grad(self.Y, self.X, self.W, self.B, h, lr, activation)
            loss_history.append(self.MSE(self.Y, self.forward(self.X, self.W, self.B, activation)))
        print(
            f"\nInitial Loss: {loss_history[0]}\nFinal Loss: {loss_history[-1]}\nMin Loss: {min(loss_history)}\n"
        )
        return loss_history

    def predict(self, X):
        for i in range(len(self.W)):
            if self.activation:
                if i == len(self.W) - 1:
                    X = self.sigmoid(X @ self.W[i] + self.B[i])
                else:
                    X = self.relu(X @ self.W[i] + self.B[i])
            else:
                X = X @ self.W[i] + self.B[i]
        return X