"""
Maximum Depth of Binary Tree - Easy #104

Given a binary tree, find the maximum depth of the tree
Maximum depth is the number of nodes in the longest path from root to furthest leaf node

Note: The depth of a node is the number of edges from the node to the tree's root node.
A root node will have a depth of 0.

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
class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    # If there's no node on the tree, the depth is 0
    if (root is None):
        return 0

    # If we've reached the leaf nodes, the depth is 1
    if (root.left is None and root.right is None):
        return 1

    # Find the depth of the left and right subtrees
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    # Find the maximum depth of the current node's left and right subtree,
    # and add 1 to count the edge between the current node and it's subtrees
    return max(left, right) + 1
        
"""
Time Complexity : O(n)
Space Complexity: O(h) 

Due to the recursive nature of the solution, space complexity is O(h) where h is the height of the tree
"""