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

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
    # Since we're searching for the maximum path, initialize the answer as negative infinity
    ans = -float("inf")

    def solution(self, root: TreeNode):
        # If we don't any have node in the tree, return 0
        if (root is None):
            return 0

        # Search for the sum of the left and right subtrees
        left = self.solution(root.left)
        right = self.solution(root.right)

        # Actual logic:
        # maxSide: Check if the current node is the root of the maximum path sum
        #          Find whether the left or right subtree's path sum is greater,
        #          then check if the path sum is greater if we add the current node's value
        # maxTop: Check if the current node is the center of the maximum path sum
        #         Check if using only one side is greater, or if using both sides is greater
        maxSide = max(root.val, max(left, right) + root.val)
        maxTop = max(maxSide, left + right + root.val)

        # At this point, maxTop will have the greater of the maxSide and maxTop
        # Compare the maxTop with the currently found maximum path sum in self.ans
        self.ans = max(self.ans, maxTop)

        # Return the maxSide, so the maximum path sum upto the current node can be used on the returned recurisve call
        return maxSide

    def maxPathSum(self, root: TreeNode) -> int:
        # Call a helper function to find the maximum sum path
        self.solution(root)
        return self.ans

        
"""
Time Complexity : O()
Space Complexity: O()
"""