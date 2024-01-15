impl Solution {
    pub fn minimum_right_shifts(nums: Vec<i32>) -> i32 {
        let mut nums_mut = nums.clone();
        for i in 0..nums_mut.len() {
            if Self::is_sorted(&nums_mut) {
                return i as i32
            }
            let last_element = nums_mut.pop();
            match last_element {
                Some(n) => nums_mut.insert(0, n),
                None => return -1
            }
        }
        -1
    }
    
    fn is_sorted<T:Ord>(nums: &Vec<T>) -> bool {
        nums.iter().zip(nums.iter().skip(1)).all(|(a, b)| a <=b)
    }
}