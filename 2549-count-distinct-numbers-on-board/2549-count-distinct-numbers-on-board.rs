impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        if n == 0 || n == 1 {
            return 1;
        }

        let mut board = vec![n];
        let mut index = 0;

        while index < board.len() {
            let current_value = board[index];

            for i in 2..current_value {
                if current_value % i == 1 && !board.contains(&i) {
                    board.push(i);
                }
            }

            index += 1
        }

        board.len() as i32
    }
}