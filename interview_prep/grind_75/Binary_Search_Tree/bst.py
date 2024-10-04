# Define the TreeNode class for the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to insert a node into the binary search tree
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root


# Function to convert the list into a binary search tree
def list_to_bst(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

def print_bst(root):
    inorder_traversal(root)