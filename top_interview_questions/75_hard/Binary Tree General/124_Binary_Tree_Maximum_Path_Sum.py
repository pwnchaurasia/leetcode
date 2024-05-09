# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findMaxPathSum(node):
            nonlocal maxi
            if not node:
                return 0
            left = max(findMaxPathSum(node.left), 0)
            right = max(findMaxPathSum(node.right), 0)
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val

        maxi = float('-inf')
        findMaxPathSum(root)
        return maxi