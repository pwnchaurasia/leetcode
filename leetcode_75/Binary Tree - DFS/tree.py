class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    if not arr:
        return None

    def build_tree(index):
        if index >= len(arr) or arr[index] is None:
            return None

        node = TreeNode(arr[index])
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        return node

    return build_tree(0)

def print_level_order(root):
    if not root:
        return

    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=" ")

root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

tree1 = list_to_tree(root1)
tree2 = list_to_tree(root2)

print("Tree 1:")
print_level_order(tree1)
print("\nTree 2:")
print_level_order(tree2)
