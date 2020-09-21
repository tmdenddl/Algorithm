"""
Binary Tree Maximum Path Sum - Hard #124

Given a non-empty binary tree, find the maximum path sum.


Note: 
- A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
- The path must contain at least one node and does not need to go through the root.




Example:

Input: 
    1
   / \
  2   3


Output:
6 (2 -> 1 -> 3)

Input: 
    -10
   /    \
  9      20
        /  \
       15   7

Output:
42 (15 -> 20 -> 7)

"""

class Solution:
    ans = -float("inf")

    def solution(self, root: TreeNode):
        if (root is None):
            return 0

        left = self.solution(root.left)
        right = self.solution(root.right)

        maxSide = max(root.val, max(left, right) + root.val)
        maxTop = max(maxSide, left + right + root.val)

        self.ans = max(self.ans, maxTop)
        return maxSide

    def maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        return self.ans

        
"""
Time Complexity : O()
Space Complexity: O()
"""