"""
Kth Smallest Element in a BST - Medium #230

Given a binary search tree, find the kth smallest element in the tree

Tips:
- We need to utilize the fact that binary search trees are already sorted.
- In-Order traversal will travel the node from the smallest first then largest last
  (LEFT ROOT RIGHT)


Example:

Input: 
       5
     /   \
    3     7
   / \    
  1   4  

k: 2

Output:
3
"""

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        
        # During the inOrder recursive callback function,
        # we'll find the kth smallest node and assign the node to self.result variable
        self.inOrder(root)
        
        return self.result

    def inOrder(self, root: TreeNode):
        if root is None:
            return

        # LEFT
        self.inOrder(root.left)

        # ROOT
        # This logic gets executed from the left bottom leaf node which is the smallest node in the tree
        # Then we decrement the k by 1 everytime. When k becomes 0, we've found the kth smallest node
        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return
        
        # RIGHT
        self.inOrder(root.right)

"""
Time Complexity : O(n)
Space Complexity: O(n)
"""