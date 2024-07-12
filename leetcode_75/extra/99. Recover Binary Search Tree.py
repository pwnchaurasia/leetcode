# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            if node.left and node.left.val > node.val:
                node.val, node.left.val = node.left.val, node.val
                dfs(node.left)

            if node.right and node.right.val > node.val:
                node.val, node.right.val = node.right.val, node.val
                dfs(node.right)

        dfs(root)
        return root
