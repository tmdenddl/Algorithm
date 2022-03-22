"""
Binary Tree Level Order Traversal - Medium #103

Given a binary tree, return the level order traversal of its nodes' values
(from left to right, level by level)

Note: This can be achieved by BFS

Example:

Input:
        10
      /    \
    5       20
  /       /    \
8       3       7
              /   \
            1       2

Output:

[
    [10], 
    [5,20], 
    [8, 3, 7],
    [1, 2]
]
"""

from typing import List
from collections import dequeue

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Initialize the answer array
        ans = []

        # If root is invalid, return empty array
        if (root is None):
            return ans
        
        # Initialize queue with root added
        q = dequeue([root])

        # While the queue is not empty
        while(q):
            # Find the current length of the queue
            n = len(q)
            # Create a temp array that will hold the current row
            temp = []

            # Iterate over the nodes currently in the queue
            for i in range(0, n):
                # remove the first node in the queue
                # then add it's value to the temp array
                f = q.popleft()
                temp.append(f.val)

                # If there is a left or right child of the current node,
                # add the children to the queue
                if (f.left is not None):
                    q.append(f.left)
                if (f.right is not None):
                    q.append(f.right)

            # If the temp array is not empty,
            # append the temp array to answer array
            # then clear the temp array for later use again
            if (len(temp) > 0):
                ans.append(temp)
                temp.clear()

        return ans

        
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""