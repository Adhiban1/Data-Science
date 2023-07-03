use std::fs::{read_to_string, write};

#[allow(unused)]
fn split(a:String, sep:&str) -> Vec<String> {
    a.split(sep)
     .map(|x| x.to_string())
     .collect::<Vec<String>>()
}

#[allow(unused)]
pub fn read_csv(path:&str) -> Vec<Vec<f32>>{
    let data = read_to_string(path).unwrap();
    let data = split(data, "\n");
    let mut data2 = vec![];
    for i in data {
        data2.push(split(i, ","));
    }
    let mut data3 = vec![vec![0.0;data2[0].len()];data2.len()];
    for i in 0..data2.len() {
        for j in 0..data2[0].len() {
            data3[i][j] = data2[i][j].parse::<f32>().unwrap();
        }
    }
    data3
}

#[allow(unused)]
pub fn write_csv(v:&Vec<Vec<f32>>, path:&str) {
    let mut a = String::new();
    for i in 0..v.len() {
        for j in 0..v[0].len() {
            a.push_str(&v[i][j].to_string());
            if j != v[0].len() - 1 {
                a.push(',');
            }
        }
        if i != v.len() - 1 {
            a.push('\n');
        }
    }
    write(path, a).unwrap();
}