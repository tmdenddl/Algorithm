## Tree
A Tree is a connected acyclic undirected graph.

#### Connected Graph
A graph is called connected if, given any two nodes there is a path between them

#### Acyclic Graph
A graph having no cycles

#### Undirected Graph
A graph whose edges are bi-directional, meaning that they can go both ways

### Terminology of a Tree:
- Path: sequence of nodes connected together in a tree
- Parent: a node above another node connected by it's edge
- Child: a node below another node conencted by it's edge
- Root: The node at the top of the tree. There's only one root per tree and one path from the root node to any node. A root has NO parents
- Leaf Node: A node with no children nodes
- Tree Height: The number of edges on the longest downard path between the root and a leaf

## m-ary Trees
Every internal vertex of the tree has no more than m children

### Binary Trees
Every node in a binary tree has at most 2 children

##### Balanced Binary Tree
A binary tree in which the depth of the two subtrees of every node never differ by more than 1

##### Unbalanced Binary Tree
A binary tree in which the depth of the two subtrees of a node differ by more than 1

#### Bianry Tree Traversal
There are three types of traversal:
- Pre-Order Traversal
- In-Order Traversal
- Post-Order Traversal

As the name indicates, the traversal algorithm visits the root node in relation to its trees.
- For pre-order traversal, root will be visited first: ROOT LEFT RIGHT
- For in-order traversal, root will be visited second: LEFT ROOT RIGHT
- For post-order traversal, root will be visited last: LEFT RIGHT ROOT

### Binary Search Tree (BST)
A binary tree that have 2 properties:
1. Left sub-tree of a node have values lower than or equal to the parent node
2. Right sub-tree of a node have values bigger than the parent node

#### Insertion on BST
When inserting elements, you have to keep the BST properties. We'll always add the new node as a leaf

#### Deletion on BST
When deleting a node from a BST, we have 3 cases:
1. Deletion on a leaf node. This is simplest case. Find the node and delete from the tree.
2. Deletion of a node with one child. Find and delete the node, and connect it's parent to it's child.
3. Deletion of a node with two children. Find and delete the node, and replace the node with the minimum node from the right subtree.