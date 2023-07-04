use std::io::Write;
use crate::matrix::{rand_matrix, dot, rand_vec, add_arr2_arr1, mse};

#[allow(unused)]
pub struct NN{
    x:Vec<Vec<f32>>,
    y:Vec<Vec<f32>>,
    hidden_layers:Vec<usize>,
    layers:Vec<usize>,
    w:Vec<Vec<Vec<f32>>>,
    b:Vec<Vec<f32>>,
    activation:bool
}

fn weights(neurons:&Vec<usize>) -> Vec<Vec<Vec<f32>>> {
    let mut w = vec![];
    for i in 0..(neurons.len() - 1) {
        w.push(rand_matrix(neurons[i], neurons[i + 1], 0.0, 1.0));
    }
    return w;
}

fn bias(neurons:&Vec<usize>) -> Vec<Vec<f32>> {
    let mut b = Vec::new();
    for i in 1..neurons.len() {
        b.push(rand_vec(neurons[i]));
    }
    return b
}

impl NN {
    pub fn new(x:Vec<Vec<f32>>, y:Vec<Vec<f32>>, hl:Vec<usize>) -> Self {
        let mut layers = hl.clone();
        layers.insert(0, x[0].len());
        layers.push(y[0].len());
        Self {x,y,hidden_layers:hl,layers:layers.clone(),
            w:weights(&layers),b:bias(&layers),
            activation:false}
    }

    #[allow(unused)]
    pub fn forward(&self) -> Vec<Vec<f32>> {
        let mut z = self.x.clone();
        for i in 0..self.w.len() {
            z = add_arr2_arr1(&dot(&z, &self.w[i]), &self.b[i]);
        }
        return z;
    }

    #[allow(unused)]
    fn modify_forward(&self, w:&mut Vec<Vec<Vec<f32>>>, b:&mut Vec<Vec<f32>>, h:f32, hn:usize, hi:usize, hj:usize, w_or_b:char) -> Vec<Vec<f32>>{
        if w_or_b == 'w'{
            w[hn][hi][hj] += h
        }
        else {
            b[hn][hi] += h
        }

        let mut z = self.x.clone();
        for i in 0..w.len() {
            z = add_arr2_arr1(&dot(&z, &w[i]), &b[i]);
        }
        return z;
    }

    #[allow(unused)]
    fn grad(&self, h:f32, lr:f32) -> (Vec<Vec<Vec<f32>>>, Vec<Vec<f32>>) {
        // Weights
        let mut w = self.w.clone();
        let mut b = self.b.clone();
        for wt in 0..w.len() {
            for wti in 0..w[wt].len() {
                for wtj in 0..w[wt][0].len() {
                    let f1 = self.modify_forward(&mut w, &mut b, h, wt, wti, wtj, 'w');
                    let f2 = self.modify_forward(&mut w, &mut b, -h, wt, wti, wtj, 'w');
                    let gradient = (mse(&self.y, &f1) - mse(&self.y, &f2)) / (2.0 * h);
                    w[wt][wti][wtj] -= lr * gradient;
                }
            }
        }

        // Bias
        for i in 0..b.len() {
            for j in 0..b[i].len() {
                let f1 = self.modify_forward(&mut w, &mut b, h, i, j, 0, 'b');
                let f2 = self.modify_forward(&mut w, &mut b, -h, i, j, 0, 'b');
                let gradient = (mse(&self.y, &f1) - mse(&self.y, &f2)) / (2.0 * h);
                b[i][j] -= lr * gradient;
            }
        }
        return (w, b);
    }

    #[allow(unused)]
    pub fn backpropagation(&mut self, h:f32, lr:f32, epochs:usize) -> Vec<f32> {
        let mut loss_history = vec![];
        loss_history.push(mse(&self.y, &self.forward()));
        for e in 0..epochs {
            (self.w, self.b) = self.grad(h, lr);
            let l = mse(&self.y, &self.forward());
            loss_history.push(l);
            print!("\rEpoch: {:4} ({}%), Loss: {:.5} ({:.2}%)  ", e+1, (e+1)*100/epochs, l, (l-loss_history[0])*100.0/loss_history[0]);
            std::io::stdout().flush().unwrap();
        }
        println!("\nInitial Loss: {}\nFinal Loss: {}\n", 
        loss_history[0], 
        loss_history[loss_history.len()-1]);
        return loss_history;
    }

    #[allow(unused)]
    pub fn predict(&self, x:&Vec<Vec<f32>>) -> Vec<Vec<f32>> {
        let mut z = x.clone();
        for i in 0..self.w.len() {
            z = add_arr2_arr1(&dot(&z, &self.w[i]), &self.b[i]);
        }
        return z;
    }
}