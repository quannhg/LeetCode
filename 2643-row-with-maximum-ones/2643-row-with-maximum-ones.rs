impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = vec![0,0];
        
        for (index, row) in mat.iter().enumerate() {
            let current_amount_one = row.iter().filter(|&&i| i == 1).count() as i32;
            
            if current_amount_one > result[1] {
                result = vec![index as i32, current_amount_one];
            }
        }
        
        result
    }
}