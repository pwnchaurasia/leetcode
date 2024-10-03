# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from interview_prep.grind_75.Binary_Tree_DFS.tree_builder import build_tree

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = {0: 1}
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val

            path_count = prefix_sums.get(curr_sum -targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0)+1
            print("--prefix_sums", prefix_sums)
            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)

            prefix_sums[curr_sum] -= 1
            return path_count
        return dfs(root, 0)


if __name__ == '__main__':
    sol = Solution()
    # root = [3,1,4,3,None,1,5]
    root = [10,5,-3,3,2,None,11,3,-2,None,1]
    targetSum = 8
    head1 = build_tree(root)
    print(sol.pathSum(head1, targetSum))