impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut maximum_wealth = 0;
        for wealth in accounts {
            if wealth.iter().sum::<i32>() > maximum_wealth {
                maximum_wealth = wealth.iter().sum();
            }
        }
        maximum_wealth
    }
}