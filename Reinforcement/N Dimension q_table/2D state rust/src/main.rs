use rand::Rng;

fn max(a:f64, b:f64, c:f64, d:f64) -> f64 {
    if a > b && a > c && a > d{
        a
    } else if b > c && b > d {
        b
    } else if c > d {
        c
    } else {d}
}

fn main() {
    let mut rng = rand::thread_rng();

    let env = [
        [0.0, -1.0,  0.0, 0.0],
        [0.0, -1.0,  0.0, 0.0],
        [0.0,  0.0, 10.0, 0.0],
        [0.0,  0.0,  0.0, 0.0]];
    let mut q = [[[0.0;4];4];4];
    let mut state:[usize;2] = [0, 0];

    for _ in 0..1000 {
        let mut action:[i32;2] = [[-1,0],[1,0],[0,-1],[0,1]][rng.gen_range(0..4)];
        let mut next_state = [(state[0] as i32 + action[0]), (state[1] as i32 + action[1])];

        if next_state[0] > env.len() as i32 - 1 {
            next_state[0] -= 2;
            action = [-1, 0];
        }
        else if next_state[0] < 0 {
            next_state[0] += 2;
            action = [1, 0];
        }
        if next_state[1] > env[0].len() as i32 - 1 {
            next_state[1] -= 2;
            action = [0, -1];
        }
        else if next_state[1] < 0 {
            next_state[1] += 2;
            action = [0, 1];
        }

        let next_state = [next_state[0] as usize, next_state[1] as usize];

        let mut temp = 0;
        if action == [-1,0] {
            temp = 0;
        }
        else if action == [1,0] {
            temp = 1;
        }
        else if action == [0,-1] {
            temp = 2;
        }
        else if action == [0,1] {
            temp = 3;
        }

        let action = temp;

        if env[state[0]][state[1]] != 0.0 {
            q[state[0]][state[1]][0] = env[state[0]][state[1]];
            q[state[0]][state[1]][1] = env[state[0]][state[1]];
            q[state[0]][state[1]][2] = env[state[0]][state[1]];
            q[state[0]][state[1]][3] = env[state[0]][state[1]];
        } else {
            q[state[0]][state[1]][action] = env[next_state[0]][next_state[1]] + 0.9 * max(q[next_state[0]][next_state[1]][0], q[next_state[0]][next_state[1]][1], 
                q[next_state[0]][next_state[1]][2], q[next_state[0]][next_state[1]][3])
        }

        state = next_state
    }
    for i in q {
        println!("{:?}", i);
    }
}
