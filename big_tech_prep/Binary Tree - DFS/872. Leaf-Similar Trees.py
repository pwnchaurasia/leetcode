from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def dfs(node, lst):
            if not node:
                return

            if not node.left and not node.right:
                lst.append(node.val)

            dfs(node.left, lst)
            dfs(node.right, lst)

        dfs(root1, leaf1)
        dfs(root2, leaf2)

        # print(leaf1)
        # print(leaf2)
        return leaf1 == leaf2

