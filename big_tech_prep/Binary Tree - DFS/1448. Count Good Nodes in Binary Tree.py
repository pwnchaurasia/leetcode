# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if not node:
                return 0

            good = 1 if node.val >=current_max else 0
            current_max = max(current_max, node.val)

            left = dfs(node.left, current_max)
            right = dfs(node.right, current_max)
            return good + left + right
        return dfs(root, root.val)

