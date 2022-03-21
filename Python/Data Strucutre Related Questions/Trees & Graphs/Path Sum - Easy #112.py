"""
Path Sum - Easy #112

Given a binary tree and a target, find if a root to leaf path exists
where summation of all elements on the path equals target

Example:

Input: 
       5
     /   \
    6     9
   /     / \
  15    11  3
 /  \         \
2    8         2

target = 34

Output:
True
"""

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
  # root = root of the current tree
  # sum = target number
  # cur = current sum
  def hasSum(self, root: TreeNode, sum: int, cur: int) -> bool:
    # If the current node is None, return False
    if (root is None):
      return False

    # Add the current node's value to the current sum
    cur += root.val

    # If the current sum equals to the target number and we've reached the leaf nodes, return True
    if (cur == sum and root.left is None and root.right is None):
      return True
    
    # Otherwise, search if we can reach the target number on either of the left or the right subtrees
    return (self.hasSum(root.left, sum, cur) or self.hasSum(root.right, sum, cur))

  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    # Call a recursive function to search through every possible subtrees
    return self.hasSum(root, sum, 0)

"""
Time Complexity : O(n)
Space Complexity: O(n)
"""