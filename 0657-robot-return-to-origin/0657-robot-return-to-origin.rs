impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut starting_point = (0, 0);

        for direction in moves.chars() {
            if direction == 'R' {
                starting_point.0 += 1;
            } else if direction == 'L' {
                starting_point.0 -= 1;
            } else if direction == 'U' {
                starting_point.1 += 1;
            } else if direction == 'D' {
                starting_point.1 -= 1;
            } else {
                // Invalid move, early return
                return false;
            }
        }

        starting_point == (0, 0)
    }
}