// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::check_length(root).is_some()
    }

    fn check_length(root: Option<Rc<RefCell<TreeNode>>>) -> Option<i32> {
        match root {
            Some(node) => {
                let left_height = Self::check_length(node.borrow().left.clone());
                let right_height = Self::check_length(node.borrow().right.clone());
                match (left_height, right_height) {
                    (Some(l), Some(r)) if (l-r).abs() <= 1 => Some(1+l.max(r)),
                    _ => None
                }
            }
            None => Some(0)
        }
    }
}