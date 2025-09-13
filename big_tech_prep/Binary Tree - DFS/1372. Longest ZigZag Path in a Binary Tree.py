# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, dir, length):
            if not node:
                return 0

            self.max_len = max(self.max_len, length)

            if dir == 'l':
                dfs(node.right, "r", length + 1)
                dfs(node.left, "l", 1)  # restart if go same direction
            else:
                dfs(node.left, 'l', length+1)
                dfs(node.right, "r", 1)

        dfs(root.left, "l", 1)
        dfs(root.right, "r", 1)
        return self.max_len




