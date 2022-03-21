"""
Serialize and Deserialize Binary Tree - Hard #297

Design an algorithm to serialize and deserialize a binary tree

Note:
Serialization is the process of converting a data structure or object into a sequence of bits
Deserialization is the process of converting that sequence of bits to the original data structure

How are we going to serailize?
- We'll apply pre-order traversal
- Separate current node with value from the next character by #
- Represent null node with X

Example:

Serialization
Input: 
       1
     /   \
    2     3
         / \    
        4   5  

Output:
1#2#X#X#3#4#X#X#5#X#X

Deserialization
Input: 
1#2#X#X#3#4#X#X#5#X#X

Output:
       1
     /   \
    2     3
         / \    
        4   5  

"""

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

class Solution:
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string
        """
        # If the node is null, return X and separate the nodes with #
        if (root is None):
            return "X#"

        # Serailize the left subtree, then the right subtree
        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        # Actual logic of serialization: we're going to separate each nodes with #
        # Remember we're using pre-order traversal: we'll visit the root node, then the left subtree, and finally the right subtree
        return str(root.val) + "#" + leftSerialized + rightSerialized

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes a string to a binary tree
        """
        # This helper function will contain the logic for deserialization
        def dfs():
            # Get the next value from the data
            val = next(data)
            # 'X' means we have no node
            if val == 'X':
                return None
            
            # Create a node with the current value
            node = TreeNode(int(val))

            # Set the current node's left and right subtree
            node.left = dfs()
            node.right = dfs()

            # Return the current node, so the recursive call up the stack will be able to
            # assign the current node as the left or right child of the parent node
            return node

        # Get rid of the separator (#), and call a helper function
        data = iter(data.split("#"))
        return dfs()

"""
Time Complexity : O(n)
Space Complexity: O(n)
"""