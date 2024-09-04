# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.deep_level = 0
        self.curr_sum = 0

        def dfs(node, level):
            if not node:
                return

            if level == self.deep_level:
                self.curr_sum += node.val
            elif level > self.deep_level:
                self.deep_level = level
                self.curr_sum = node.val

            dfs(node.left, level+1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return self.curr_sum
