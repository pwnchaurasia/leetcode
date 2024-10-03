# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self._max_length = 0

        def dfs(node, length, direction):
            if not node:
                return 0

            self._max_length = max(self._max_length, length)

            if direction == 'left':
                dfs(node.left, length+1, "right")
                dfs(node.right, 1, "left")
            else:
                dfs(node.right, length + 1, "left")
                dfs(node.left, 1, "right")

        dfs(root.left, 1, "right")
        dfs(root.right, 1, "left")
        return self._max_length