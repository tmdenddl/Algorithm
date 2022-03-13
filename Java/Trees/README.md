## Trees

### Trees
- Hierarchical data structure
- Every item in the tree is a node
- Each node has a value and a pointer to its child node
  - Node with no parent is called a root
  - Node with no children are called leaf
  - Pointer to another node is called an edge
- Every non-root node has one and only one parent
  - A leaf node has no children
  - A singleton tree has only one node - the root
- A height of the tree is the number of edges on longest path from the node to the leaf
- A depth of the tree is the number of edges from the node to the root
- A level of the tree contains all the nodes that are at the same depth

### Binary Tree
- Every node has 0, 1, or 2 children
- Children are referred to as left child and right child
- In practice, we use binary search trees (BST)
- Binary tree is complete if every level, except the last level, has two children
  - On the last level, all the nodes are as left as possible
- Binary tree is full if every node other than the leaves needs to have two children
  - Full binary trees are also considered as complete binary trees

### Binary Search Tree (BST)
- Can perform insertions, deletions, and retrievals in O(log n) time complexity
- The left child always has a smaller value than its parent
- The right child always has a larger value than its parent
- This means everything to the left of the root is less than the value of the root
- Likewise, everything to the right of the root is greater than the value of the root
- Because of that, we can do a binary search on this tree


### Traversal
- Level: visit nodes on each level
- Pre-order: visit the root of every subtree first
- Post-order: visit the root of every subtree last
- In-order: visit left child, then root, then right child

#### Example Tree
            25
           /   \
          20    27
         /  \   / \
        15  22 26  30
                   / \
                  29  32

Level Order: 25, 20, 27, 15, 22, 26, 30, 29, 32
Pre-order: 25, 20, 15, 22, 27, 26, 30, 29, 32
Post-order: 15, 22, 20, 26, 29, 32, 30, 27, 25
In-order: 15, 20, 22, 25, 26, 27, 29, 30, 32

Think of pre-order, in-order and post-order traversal as when the root of the subtree is visited.
- Pre-order traversal will visit the root of the subtree first
- In-order traversal will visit the root of the subtree in the middle
- Post-order traversal will visit the root of the subtree last

#### Delete
There are 3 possible cases for the node to be deleted:
1. Node is a leaf
2. Node has one child
3. Node has two children

Case 1: Simple deletion of the node. Remove pointer from the parent node.
Case 2: Replace the node we're deleting with its child.
Case 3: This is complex...
- Need to figure out what the replacement node will be from the children nodes
- Want minimal disruption to the existing tree structure
- Can take the replacement node from the deleted node's left subtree or right subtree
- If taking it from the left subtree, we have to take the largest value in the left subtree
- If taking it from the right subtree, we have to take the smallest value in the right subtree
- Choose one and stick to it
