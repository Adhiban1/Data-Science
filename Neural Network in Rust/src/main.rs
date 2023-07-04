mod neural_network;
mod matrix;
use neural_network::NN;
use matrix::rand_matrix;

fn main() {
    let x = rand_matrix(100, 10, -1.0, 1.0);
    let y = rand_matrix(100, 1, -1.0, 1.0);
    let mut nn = NN::new(x, y, vec![4, 4]);
    nn.backpropagation(0.01, 0.01, 200);
}