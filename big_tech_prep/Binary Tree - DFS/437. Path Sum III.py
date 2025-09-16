from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs_from(node, target):
            if not node:
                return 0

            count = 1 if node.val == target else 0
            count += dfs_from(node.left, target=target-node.val)
            count += dfs_from(node.right, target=target-node.val)
            return count

        def dfs(node):

            if not node:
                return 0

            return (
                dfs_from(node, target=targetSum) +
                dfs(node.left) +
                dfs(node.right)
            )

        return dfs(node=root)

