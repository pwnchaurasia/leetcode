# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def path_sum_a(root, s):
            if not root:
                return 0
            res = 0
            if root.val == s:
                res += 1
            res += path_sum_a(root.left, s-root.val)
            res += path_sum_a(root.right, s-root.val)
            return res

        if not root:
            return 0
        return (self.pathSum(root.left, targetSum=targetSum) +
                path_sum_a(root, targetSum) +
                self.pathSum(root.right, targetSum=targetSum))


