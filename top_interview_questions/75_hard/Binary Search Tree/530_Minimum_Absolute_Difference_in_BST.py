# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float('inf')

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, abs(node.val - prev.val))
            prev = node
            dfs(node.right)
        dfs(root)
        return res