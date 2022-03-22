"""
Binary Tree Postorder Traversal - Medium #145 

Given a binary tree, return the postorder traversal of its nodes' values
(LEFT RIGHT ROOT)

Example:

Input:
       3
     /    \
   2       5
  /      /    \
1       4      6

Output:

[1, 2, 4, 6, 5, 3]

"""

from typing import List
from collections import dequeue

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
    def postOrder(self, root: TreeNode) -> List[List[int]]:
        # If root is invalid, return
        if (root is None):
            return ans

        # Initialize the answer array, and two stacks:
        # s1 = Stack used to process the node in the correct order that we want them to be processed in.
        #      This one will be the substitute for the call stack that we would have in a recursive solution
        # s2 = Stack that we just push the nodes onto for the final solution.
        #      This one will act as the container of our solution
        ans = []
        s1 = []
        s2 = []

        # Append the root to s1
        s1.append(root)

        # Loop over until s1 is not empty
        while(s1):
            # Get and remove the top of the stack s1
            # Append the element obtained to stack s2
            x = s1[-1]
            s1.pop()
            s2.append(x)

            # If there are any child of the current node,
            # append the children to the stack s1
            if (x.left):
                s1.append(x.left)
            if (x.right):
                s1.append(x.right)

        # While the stack is not empty
        while(s2):
            # Get and remove the top of the stack s2
            # Append the element obtained to an answer array
            y = s2[-1]
            s2.pop()
            ans.append(y.val)

        return ans
 
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""