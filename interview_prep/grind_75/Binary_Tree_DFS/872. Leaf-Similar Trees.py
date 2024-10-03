# Definition for a binary tree node.
from typing import Optional
from interview_prep.grind_75.Binary_Tree_DFS.tree_builder import build_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1, list2 = [], []

        def dfs(root, lst):
            if not root:
                return None
            if not root.left and not root.right:
                lst.append(root.val)
            dfs(root.left, lst)
            dfs(root.right, lst)

        dfs(root1, list1)
        dfs(root2, list2)
        return list1 == list2


if __name__ == '__main__':
    sol = Solution()
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    head1 = build_tree(root1)
    head2 = build_tree(root2)
    sol.leafSimilar(head1, head2)