use rand::Rng;

#[allow(unused)]
pub fn dot(a:&Vec<Vec<f32>>, b:&Vec<Vec<f32>>) -> Vec<Vec<f32>> {
    let (i, j, k) = (a.len(), a[0].len(), b[0].len());
    let mut c = vec![vec![0.0;k];i];
    for i1 in 0..i {
        for k1 in 0..k {
            for j1 in 0..j {
                c[i1][k1] += a[i1][j1]*b[j1][k1];
            }
        }
    }
    c
}

// Addition
#[allow(unused)]
pub fn m_sum(a:&Vec<Vec<f32>>, b:&Vec<Vec<f32>>) -> Vec<Vec<f32>> {
    let (l, m) = (a.len(), a[0].len());
    let mut c = vec![vec![0.0;m];l];
    for i in 0..l {
        for j in 0..m {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    c
}

#[allow(unused)]
pub fn s_sum(a:&Vec<Vec<f32>>, b:f32) -> Vec<Vec<f32>> {
    let (l, m) = (a.len(), a[0].len());
    let mut c = vec![vec![0.0;m];l];
    for i in 0..l {
        for j in 0..m {
            c[i][j] = a[i][j] + b;
        }
    }
    c
}

// Multiplication
#[allow(unused)]
pub fn m_mul(a:&Vec<Vec<f32>>, b:&Vec<Vec<f32>>) -> Vec<Vec<f32>> {
    let (l, m) = (a.len(), a[0].len());
    let mut c = vec![vec![0.0;m];l];
    for i in 0..l {
        for j in 0..m {
            c[i][j] = a[i][j] * b[i][j];
        }
    }
    c
}

#[allow(unused)]
pub fn s_mul(a:&Vec<Vec<f32>>, b:f32) -> Vec<Vec<f32>> {
    let (l, m) = (a.len(), a[0].len());
    let mut c = vec![vec![0.0;m];l];
    for i in 0..l {
        for j in 0..m {
            c[i][j] = a[i][j] * b;
        }
    }
    c
}

// Sum of all elements in matrix
#[allow(unused)]
pub fn sum(a:&Vec<Vec<f32>>) -> f32 {
    let mut temp = 0.0;
    for i in a {
        for j in i {
            temp += j;
        }
    }
    temp
}

// Matrix Mean
#[allow(unused)]
pub fn mean(a:&Vec<Vec<f32>>) -> f32 {
    let mut temp = 0.0;
    let mut n = 0.0;
    for i in a {
        for j in i {
            temp += j;
            n += 1.0;
        }
    }
    temp / n
}

// Random
#[allow(unused)]
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

#[allow(unused)]
pub fn rand_vec(l:usize) -> Vec<f32> {
    let mut r = rand::thread_rng();
    let mut v = Vec::new();
    for _ in 0..l {
        v.push(r.gen());
    }
    return v;
}

#[allow(unused)]
pub fn add_arr2_arr1(a:&Vec<Vec<f32>>, b:&Vec<f32>) -> Vec<Vec<f32>> {
    let mut c = vec![vec![0.0; a[0].len()];a.len()];
    for i in 0..a.len() {
        for j in 0..a[0].len() {
            c[i][j] = a[i][j] + b[j];
        }
    }
    return c;
}

#[allow(unused)]
pub fn mse(a:&Vec<Vec<f32>>, b:&Vec<Vec<f32>>) -> f32 {
    let mut e = 0.0;
    for i in 0..a.len() {
        for j in 0..a[0].len() {
            e += (a[i][j] - b[i][j]).powi(2);
        }
    }
    e = e / ((a.len() as f32)*(a[0].len() as f32));
    return e;
}