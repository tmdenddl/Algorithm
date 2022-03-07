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

class Solution:
    def hasSum(self, root: TreeNode, sum: int, cur: int) -> bool:
        if (root is None):
          return False

        cur += root.val
        if (cur == sum and root.left is None and root.right is None):
          return True
        
        return (self.hasSum(node.left, sum, cur) or self.hasSum(node.right, sum, cur))

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasSum(root, sum, 0)

        
    
    

        

        
"""
Time Complexity : O(N)
Space Complexity: O(N)
"""