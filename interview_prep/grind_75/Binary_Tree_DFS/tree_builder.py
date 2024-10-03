from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:  # If the list is empty, return None
        return None

    # Initialize the root with the first value
    root = TreeNode(values[0])
    queue = deque([root])

    i = 1
    while i < len(values):
        current = queue.popleft()  # Get the current parent node from the queue

        # Add left child if it exists
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Add right child if it exists
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root