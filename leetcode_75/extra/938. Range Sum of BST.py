# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.arr = []

        def dfs(node, low, high):
            if node:
                if low <= node.val <= high:
                    self.arr.append(node.val)
                dfs(node.left, low, high)
                dfs(node.right, low, high)

        dfs(root, low=low, high=high)
        return sum(self.arr)

