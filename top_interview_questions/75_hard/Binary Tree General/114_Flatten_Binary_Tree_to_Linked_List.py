# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return []
        from collections import deque
        stack = [root]
        prev = None
        while stack:
            poped = stack.pop()
            if poped.right:
                stack.append(poped.right)
            if poped.left:
                stack.append(poped.left)
            
            if prev:
                prev.right = poped
                prev.left = None
            prev = poped
    



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flattening the binary tree into a linked list
Solution().flatten(root)

# Printing the flattened linked list (pre-order)
current_node = root
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.right
print("None")