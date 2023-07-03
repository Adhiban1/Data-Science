# Neural NetWork (From Scratch)

## Introduction
This is a Python implementation of a neural network model from scratch. The model allows you to train a neural network using provided input data (X) and corresponding output data (Y). It supports customizable parameters such as the number of hidden layers, learning rate, activation functions, epochs, and more. This documentation provides an overview of the model's usage and the available options.

## Maths

- $X$ - Input
- $Y$ - Output
- $W$ - Weights
- $B$ - Biases

Forward Propagation:

$$
\begin{matrix}
Z_1 = f(X \cdot W_1 + B_1) \\
Z_2 = f(Z_1 \cdot W_2 + B_2) \\ 
\vdots \\
Z_n = f(Z_{n-1} \cdot W_n + B_n)
\end{matrix}
$$

```python
def forward(X, W, B):
    for i in range(len(W)):
        X = activation_function(X @ W[i] + B[i]))
    return X
```

Grad:
$$\triangle w = \frac{loss(w+h) - loss(w-h)}{2h}$$

$$w \leftarrow w - lr. \triangle w$$

```python
gradient = (self.MSE(Y, f1) - self.MSE(Y, f2)) / (2 * h)
W[wt][wti][wtj] -= lr * gradient
```

## Getting Started
### Prerequisites
- Python 3.x
- NumPy library
- Matplotlib library

## Usage
1. Import the NN class from the NeuralNetwork module:

```python
from NeuralNetwork import NN
```

2. Prepare your input data (X) and output data (Y). Ensure that they are NumPy arrays of appropriate dimensions. For example: 

```python
import numpy as np
X = np.random.randn(1000, 3)
Y = np.random.randn(1000, 1)
```

Create an instance of the NN class, passing in the input data (X), output data (Y), and other desired parameters:

```python
nn = NN(X, Y, [4, 4], 0)
```

The parameters for initializing the NN class are as follows:

- **X:** Input data.
- **Y:** Output data.
- **no_of_hiddenlayers:** A list specifying the number of neurons in each hidden layer. For example, [4, 4] creates a network with two hidden layers, each containing 4 neurons.
 - **random_state:** An integer value to seed the random number generator for reproducibility.

4. Train the model using backpropagation by calling the backpropagation method, passing in the desired h value, learning rate, and number of epochs:

```python
loss_history = nn.backpropagation(0.01, 0.01, 200)
```

The parameters for the back_propagation method are as follows:

- **h:** The value used in limit approximation during backpropagation. Tuning this parameter can help improve results.
- **lr:** The learning rate, which determines the step size in updating the model's weights.
- **epochs:** The number of training iterations to perform.
Optionally, you can visualize the loss history by plotting it using the Matplotlib library:

```python
import matplotlib.pyplot as plt

plt.plot(loss_history)
plt.title("Loss")
plt.savefig('loss.png')
plt.show()
```

## Limitations and Future Improvements
This implementation of the neural network model from scratch serves as a basic starting point and does not include advanced optimizations or additional features. Some limitations and potential areas for future improvements include:

- **Limited activation function support:** Currently, the model applies the Rectified Linear Unit (ReLU) activation function for all layers except the last, where it applies the Sigmoid function.
- **Lack of optimization techniques:** The current implementation does not include optimization techniques like momentum, adaptive learning rates, or regularization. Incorporating these techniques can help improve training efficiency and prevent overfitting.
- **Scalability:** The model is designed for small-scale problems and may not scale well to larger datasets or complex architectures. Implementing techniques like mini-batch training or utilizing GPU acceleration could enhance performance on larger-scale tasks.
- **Code structure and modularity:** The current implementation is contained within a single file, which may not be suitable for larger projects. Refactoring the code into separate modules or classes could improve code organization and reusability.

Please note that the provided code and documentation serve as a starting point and should be optimized and expanded based on specific requirements and use cases.

## Conclusion
This neural network model provides a simple yet customizable implementation that allows you to train a basic neural network using backpropagation. By adjusting various parameters, such as the number of hidden layers, learning rate, activation functions, and epochs, you can explore different configurations and experiment with different datasets. Remember to optimize and expand the code as needed to suit your specific needs and improve performance.