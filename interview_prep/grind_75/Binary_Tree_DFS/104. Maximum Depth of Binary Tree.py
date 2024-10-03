# Definition for a binary tree node.
from collections import deque
from typing import Optional
from interview_prep.grind_75.Binary_Tree_DFS.tree_builder import build_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))
        return dfs(root)


if __name__ == '__main__':
    sol = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    root = [1, None, 2]
    root = build_tree(root)
    print(sol.maxDepth(root))
