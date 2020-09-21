"""
Lowest common ancestor of a binary tree - Medium #236

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree
that has both p and q as descendants


Example:

Input: 
       10
     /   \
    5     20
   /     / \
  8     3   7
           /  \
          1    2

LCA between 8 and 3?

Output:
10

"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root is None):
            return None
        
        if (root.val == p.val or root.val == q.val):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left is None and right is None):
            return None

        if (left is not None and right is not None):
            return root

        if (left is None):
            return right
        return left

        
    
    

"""
Time Complexity : O(N)
Space Complexity: O(N)
"""