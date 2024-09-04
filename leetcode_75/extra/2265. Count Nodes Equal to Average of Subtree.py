# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total_nodes = 0
        sum = 0
        while root:
            sum += root.val
            if root.left:
                root = root.left
            if root.right:
                root = root.right
            total_nodes += 1

        avg =
