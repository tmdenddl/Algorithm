"""
Symmetric Trees - Easy #101

Given a binary tree, check if this tree is a mirror of itself

Example:

Input: 
      5
   /    \
  2      2
 / \    / \
3   4  4   3

Output:
True

"""
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Solution:
    def isMirror(self, t1, t2):
        # If both right and left subtrees are None they're symmetric, thus return True
        if (t1 is None and t2 is None):
            return True
        # If either of the right or left subtree is not None they're NOT symmetric, thus return False
        if (t1 is None or t2 is None):
            return False

        # Two subtrees are symmetric if:
        # - Root of the right and left subtree are identical
        # - Right of the right subtree is a mirror of the left of the left subtree
        #   (Nodes on the outer subtree are a mirror)
        # - Left of the right subtree is a mirror of the Right of the left subtree
        #   (Nodes on the inner subtree are a mirror)
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        # Call recursive backtracking call to check if the left subtree and right subtree are symmetrical
        return self.isMirror(root.right, root.left)
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""