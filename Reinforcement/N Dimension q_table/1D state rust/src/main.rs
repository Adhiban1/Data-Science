use rand::Rng;

fn max(a:f64, b:f64) -> f64 {
    if a > b {a} else {b}
}

fn main() {
    let mut rng = rand::thread_rng();

    let env = [1.0, 0.0, 0.0, 0.0, 10.0];
    let mut q = [[0.0, 0.0];5];
    let mut state = 2;

    for _ in 0..100 {
        let mut action = rng.gen_range(0..=1);

        if state == 0 {
            action = 1;
        }
        else if state == env.len() - 1 {
            action = 0;
        }

        let move_ = if action == 1 {1.0} else {-1.0};
        let next_state = ((state as f64) + move_) as usize;

        q[state][action] = env[state] + 0.9 * max(q[next_state][0], q[next_state][1]);

        state = next_state;
    }
    println!("{:?} {}", q, state);
}
