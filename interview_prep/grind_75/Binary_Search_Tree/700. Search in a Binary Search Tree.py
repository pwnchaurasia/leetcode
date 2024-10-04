# Definition for a binary tree node.
from typing import Optional
from interview_prep.grind_75.Binary_Search_Tree.bst import list_to_bst, print_bst
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if not node or node.val == val:
                return node
            if node.val < val:
                return dfs(node.right, val)
            return dfs(node.left, val)
        return dfs(root, val)




if __name__ == '__main__':
    sol = Solution()
    root = [4, 2, 7, 1, 3]
    val = 2
    root = list_to_bst(root)
    new_r = sol.searchBST(root, val=val)
    print_bst(new_r)

