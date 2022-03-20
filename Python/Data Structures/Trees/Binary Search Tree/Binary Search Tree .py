class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, node):
    # If there's no node in the tree, set the node to root
    if(root is None):
        root = node
        return

    # If the current node (root) is smaller than the node to insert (node)
    if(root.data < node.data):
        # If there's no right child of the current node, insert the node as the right child
        if(root.right is None):
            root.right = node
        else:
        # If there's a right child of the current node, continue searching down the right subtree
            insert(root.right, node)
    # If the current node (root) is bigger than the node to insert (node)
    else:
        # If there's no left child of the current node, insert the node as the left child
        if(root.left is None):
            root.left = node
        else:
            # If there's a left child of the current node, continue searching down the left subtree
            insert(root.left, node)

def minValueNode(node):
    while(node.left is not None):
        node = node.left
    return node

def deleteNode(node, key):
    if(node is None):
        return node

    # If the key to be deleted is smaller than the node's key, search down the left subtree
    if (key < node.data):
        node.left = deleteNode(node.left, key)
    # If the kye to be delete is greater than the node's key, search down the right subtree
    elif (key > node.data):
        node.right = deleteNode(node.right, key)
    # If key is same as node's key, then this is the node to be deleted
    else:
        # Case 1 & 2: Node with only no child or one child
        # If the node has no left child, 
        # we replace the current node with the right child and delete the current node
        if (node.left is None):
            temp = node.right
            node = None
            return temp
        # If the node has no right child, 
        # we replace the current node with the left child and delete the current node
        elif (node.right is None):
            temp = node.left
            node = None
            return temp

        # Case 3: Node with two children - Get the inorder successor (Smallest of the right subtree)
        temp = minValueNode(node.right)
        # Copy the inorder successor's content to this node
        node.data = temp.data
        # Delete the inorder successor
        node.right = deleteNode(node.right, temp.data)

    return node

def search(node, key):
    print("Current Node is: ", node.data)
    # If the current node is invalid, return None
    if (node is None):
        print("No node found")
        return None

    # If the current node's data equals to the given key, we've found the node
    if (node.data == key):
        print("Node found!")
        return node
    
    # If the current node's data is smaller than the key, search down the right subtree
    if (node.data < key):
        return search(node.right, key)
    # Else if the current node's data is bigger than the key, search down the left subtree
    return search(node.left, key)

def preorder(node):
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)


#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree = Node(5)

#	         5
#       /  	      \
#     None	       None

insert(tree, Node(3))

#	         5
#       /  	      \
#     3	            None

insert(tree, Node(2))

#	         5
#       /  	      \
#     3	            None
#   /
#  2
insert(tree, Node(4))

#	         5
#       /  	      \
#     3	            None
#   /   \
#  2     4
insert(tree, Node(7))

#	         5
#       /  	      \
#     3	            7
#   /   \
#  2     4
insert(tree, Node(6))

#	         5
#       /  	      \
#     3	            7
#   /   \        /
#  2     4      6
insert(tree, Node(8))

#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8


# 5 3 2 4 7 6 8
preorder(tree)
