# Neural Network in Rust (From Scratch)

## Introduction
This is a Python implementation of a neural network model from scratch. The model allows you to train a neural network using provided input data (X) and corresponding output data (Y). It supports customizable parameters such as the number of hidden layers, learning rate, epochs, and more. This documentation provides an overview of the model's usage and the available options.

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

```rust
pub fn forward(&self) -> Vec<Vec<f32>> {
    let mut z = self.x.clone();
    for i in 0..self.w.len() {
        z = add_arr2_arr1(&dot(&z, &self.w[i]), &self.b[i]);
    }
    return z;
}
```

Grad:
$$\triangle w = \frac{loss(w+h) - loss(w-h)}{2h}$$

$$w \leftarrow w - lr. \triangle w$$

```rust
let gradient = (mse(&self.y, &f1) - mse(&self.y, &f2)) / (2.0 * h);
w[wt][wti][wtj] -= lr * gradient;
```

## Getting Started
### Prerequisites
- Rust
- rand library

## Usage
1. Import the NN class from the neural_network module:

```rust
mod neural_network;
mod matrix;
use neural_network::NN;
use matrix::rand_matrix;
```

2. Prepare your input data (X) and output data (Y). Ensure that they are `Vec<Vec<f32>>` arrays. For example: 

```rust
pub fn rand_matrix(a:usize, b:usize, start:f32, end:f32) -> Vec<Vec<f32>> {
    let mut v = vec![vec![0.0;b];a];
    let mut r = rand::thread_rng();
    for i in 0..a {
        for j in 0..b {
            v[i][j] = r.gen_range(start..=end);
        }
    }
    v
}
```

```rust
let x = rand_matrix(10, 3, 0.0, 1.0);
let y = rand_matrix(10, 1, 0.0, 1.0);
```

Create an instance of the NN, passing in the input data (X), output data (Y), and other desired parameters:

```rust
let mut nn = NN::new(x, y, vec![4, 4]);
```

The parameters for initializing the NN are as follows:

- **X:** Input data.
- **Y:** Output data.
- **no_of_hiddenlayers:** A vector specifying the number of neurons in each hidden layer. For example, vec![4, 4] creates a network with two hidden layers, each containing 4 neurons.

4. Train the model using backpropagation by calling the backpropagation method, passing in the desired h value, learning rate, and number of epochs:

```rust
nn.backpropagation(0.01, 0.01, 200);
```

The parameters for the back_propagation method are as follows:

- **h:** The value used in limit approximation during backpropagation. Tuning this parameter can help improve results.
- **lr:** The learning rate, which determines the step size in updating the model's weights.
- **epochs:** The number of training iterations to perform.

## Limitations and Future Improvements
This implementation of the neural network model from scratch serves as a basic starting point and does not include advanced optimizations or additional features. Some limitations and potential areas for future improvements include:

- **No activation function support:** Currently, activation functions are not included.
- **Lack of optimization techniques:** The current implementation does not include optimization techniques like momentum, adaptive learning rates, or regularization. Incorporating these techniques can help improve training efficiency and prevent overfitting.
- **Scalability:** The model is designed for small-scale problems and may not scale well to larger datasets or complex architectures.
- **Code structure and modularity:** The current implementation is contained within a single file, which may not be suitable for larger projects. Refactoring the code into separate modules or classes could improve code organization and reusability.

Please note that the provided code and documentation serve as a starting point and should be optimized and expanded based on specific requirements and use cases.

## Conclusion
This neural network model provides a simple yet customizable implementation that allows you to train a basic neural network using backpropagation. By adjusting various parameters, such as the number of hidden layers, learning rate, and epochs, you can explore different configurations and experiment with different datasets. Remember to optimize and expand the code as needed to suit your specific needs and improve performance.