"""
Serialize and Deserialize Binary Tree - Hard #297

Design an algorithm to serialize and deserialize a binary tree

Note:
Serialization is the process of converting a data structure or object into a sequence of bits
Deserialization is the process of converting that sequence of bits to the original data structure


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

class Solution:
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string
        """
        if (root is None):
            return "X#"

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        return str(root.val) + "#" + leftSerialized + rightSerialized

    def serialize(self, data: str) -> TreeNode:
        """
        Decodes a string to a binary tree
        """
        def dfs():
            val = next(data)
            if val == 'X':
                return None
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        data = iter(data.split("#"))
        return dfs()

    
        
    
    

"""
Time Complexity : O(N)
Space Complexity: O(N)
"""