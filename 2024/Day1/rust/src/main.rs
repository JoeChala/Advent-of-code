use std::fs;
fn main() {
    let inputs = fs::read_to_string("data.txt").expect("cannot read");
    let mut left = Vec::<i32>::new();
    let mut right = Vec::<i32>::new();

    for line in inputs.lines(){
        let mut nums = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap());
        left.push(nums.next().unwrap());
        right.push(nums.next().unwrap());
    }
    let len : i32 = left.len() as i32;
    quicksort(&mut left,0,len-1);
    quicksort(&mut right,0,len-1);
    
    //Part 1 finding sum of difference between pairs
    let mut sum : i32 = 0;
    for i in 0..len {
        let diff : i32 = left[i as usize] - right[i as usize];
        sum += diff.abs(); 
    }
    println!("Part 1 : {sum}");

    //Part 2 finding similarity score, element in left * freq in right
    let mut sim_score : i32 = 0;
    for i in 0..len {
        let count : i32 = right.iter().filter(|&&x| x == left[i as usize]).count() as i32;
        sim_score += left[i as usize] * count;
    }
    println!("Part 2 : {sim_score}");
}


fn quicksort(nums : &mut Vec::<i32>,low : i32,high : i32) {
    if low < high {
        let p = partition(nums,low,high);
        quicksort(nums,low,p-1);
        quicksort(nums,p+1,high);
    }
}
fn partition(nums : &mut Vec::<i32>,low : i32,high : i32) -> i32 {
    let pivot = nums[high as usize];
    let mut i = low;

    for j in low..high {
        if nums[j as usize] <= pivot {
            nums.swap(i as usize,j as usize);
            i += 1
        }
    }
    nums.swap(i as usize,high as usize);
    i
}
