"""
Lowest common ancestor of a binary tree - Medium #236

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree
that has both p and q as descendants

Tips:
- Think of searching recursion logic as going from the buttom upwards.
- Think of the single node. If the left subtree has one of the node, and the right subtree also has the other node.
  That means that our node is a common ancestor.
- We need to search the left/right subtrees for every node in search for our 2 target nodes,
  if we find one at each subtree, the current node is the lowest common ancestor
- What if we find either but not both of the target nodes? The current node CAN'T BE the lowest common ancestor.
  We would return the node to indicate that we found it in the current subtree.
- Remember that each call represent a question "What is the lowest common ancestor from this node?"


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

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # If there is no node in the current subtree, return None
    if (root is None):
      return None
    
    # If we've found either of the target nodes (p or q), return the root of the current subtree
    # If we've found the target node, there's no point of going down any further, 
    # we need to return the call so we can traverse back up the stack calls
    if (root.val == p.val or root.val == q.val):
      return root
    
    # Search through the left and right subtree to check if we can find the lowest common ancestor
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # If both left and right returned None, there's no target node from both the left and right subtrees
    if (left is None and right is None):
      return None

    # If we've found the target node on both left and right subtrees and those values were returned from
    # the recursive calls, return the current node as we've found the lowest common ancestor node.
    if (left is not None and right is not None):
      return root

    # We reach this point only if one of the subtrees returned None.
    # In that case, if left subtree returned None, the right subtree has the target node
    if (left is None):
      return right

    # Likewise, if only the right subtree returned None, the left subtree has the target node
    return left

        
    
    

"""
Time Complexity : O(n)
Space Complexity: O(n)
"""