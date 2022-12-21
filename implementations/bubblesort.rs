use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn bubble_sort<T: Ord>(arr: &mut [T]) {
    let i = 0;
    let mut swap_needed: bool = true;

    while i < arr.len() - 1 && swap_needed {
        swap_needed = false;
        for j in 1..arr.len() - i {
            if arr[j - 1] > arr[j] {
                arr.swap(j - 1, j);
                swap_needed = true;
            }
        }
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    let numbers_filename = std::env::args().nth(1).expect("no numbers filename given");
    let list_length: usize = std::env::args().nth(2).expect("no list length given").parse::<usize>().ok().expect("list length has to be an integer");

    let mut numbers = vec![0; list_length];
    let mut i: usize = 0;

    if let Ok(lines) = read_lines(numbers_filename) {
        for line in lines {
            if let Ok(number) = line {
                if i >= list_length {
                    break
                }
                numbers[i] = number.parse::<u32>().unwrap();
                i += 1;
            }
        }
    }

    bubble_sort(&mut numbers);
}