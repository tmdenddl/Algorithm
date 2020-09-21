"""
Maximum Depth of Binary Tree - Easy #104

Given a binary tree, find the maximum depth of the tree
Maximum depth is the number of nodes in the longest path from root to furthest leaf node


Example:

Input: 
      2
    /   \
   4     7
        / \
      12  15
         /
       18

Output:
4

"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root is None):
            return 0

        if (root.left is None and root.right is None):
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

        
    
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""