impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let mut max_diagonal = 0.0;
        let mut max_area = 0;
        for i in 0..dimensions.len() {
            let current_diagonal = ((dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1]) as f64).sqrt();
            if current_diagonal == max_diagonal {
                let current_area = dimensions[i][0] * dimensions[i][1];
                if current_area > max_area {
                    max_area = current_area
                }
            }
            else if current_diagonal > max_diagonal {
                max_diagonal = current_diagonal;
                max_area = dimensions[i][0] * dimensions[i][1];
            }
        }
        max_area
    }
}