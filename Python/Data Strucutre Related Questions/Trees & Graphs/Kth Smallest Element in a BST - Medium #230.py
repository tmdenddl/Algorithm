"""
Kth Smallest Element in a BST - Medium #230

Given a binary search tree, find the kth smallest element in the tree


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

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None

        self.inOrder(root)
        
        return self.result

    def inOrder(self, root: TreeNode):
        if root is None:
            return

        self.inOrder(root.left)

        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return
        
        self.inOrder(root.right)

        
    
    

"""
Time Complexity : O(N)
Space Complexity: O(N)
"""