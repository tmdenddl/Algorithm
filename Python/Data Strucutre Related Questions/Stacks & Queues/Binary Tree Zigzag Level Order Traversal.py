"""
Binary Tree Zigzag Order Traversal - Medium #103

Given a binary tree, return the zigzag order traversal of its nodes' values
(from left to right, then right to left for the next level and alternate between)

Note: This can be achieved by making a modification to the BFS
    - Use Dequeue 
        - Dequeue has two ends, a front and a rear, and the items remain positioned in the collection
        - New items can be added at either the front or rear
        - Likewise, existing items can be removed from either end

Example:

Input:
        3
      /    \
    9       20
          /    \
       15       7

Output:

[
    [3], 
    [20, 9], 
    [15, 7]
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
    def zigzagOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        zigzag = False

        # If root is invalid, return
        if (root is None):
            return ans
        
        # Initialize dequeue with root added
        q = dequeue()
        q.append(root)

        # While the dequeue is not empty
        while(q):
            n = len(q)
            level = []
            # Iterate over the current level
            for i in range(0, n):
                # If zigzag is true, we're traversing from right to left
                if zigzag:
                    # remove the right node from the dequeue
                    # then add it's value to the level array
                    f = q.pop()
                    level.append(f.val)

                    # If the node has children,
                    # add the children to the left of the dequeue in the order from right to left
                    if (f.right is not None):
                        q.appendleft(f.right)
                    if (f.left is not None):
                        q.appendleft(f.left)
                # If traversing from left to right
                else:
                    # remove the left node from the dequeue
                    # then add it's value to the level array
                    f = q.popleft()
                    level.append(f.val)

                    # If the node has children,
                    # add the children to the right of the dequeue in the order from left to right
                    if (f.left is not None):
                        q.append(f.left)
                    if (f.right is not None):
                        q.append(f.right)

            # If the level array is not empty,
            # append the level array to answer array
            # then clear the level array for later use again
            if (len(level) > 0):
                ans.append(level)
                level.clear()
            zigzag = not zigzag

        return ans
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""