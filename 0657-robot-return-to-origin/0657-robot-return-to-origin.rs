impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut moves_str = moves.clone();
        let mut starting_point = (0, 0);
        for direction in moves.chars() {
            match direction {
                'R' => starting_point.0 +=1,
                'L' => starting_point.0 -=1,
                'U' => starting_point.1 +=1,
                'D' => starting_point.1 -=1,
                _ => (),
            }
            moves_str.remove(0);
        }
        return starting_point == (0, 0)
    }
}