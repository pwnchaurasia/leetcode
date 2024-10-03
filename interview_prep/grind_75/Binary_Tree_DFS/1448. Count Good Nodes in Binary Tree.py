# Definition for a binary tree node.
from interview_prep.grind_75.Binary_Tree_DFS.tree_builder import build_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):

            if not node:
                return 0

            good_count = 0
            if node.val >= curr_max:
                good_count = 1
            curr_max = max(node.val, curr_max)
            good_count += dfs(node.left, curr_max)
            good_count += dfs(node.right, curr_max)
            return good_count
        return dfs(root, float('-inf'))


if __name__ == '__main__':
    sol = Solution()
    # root = [3,1,4,3,None,1,5]
    root = [2, None, 4, 10, 8, None, None, 4]
    head1 = build_tree(root)
    print(sol.goodNodes(head1))