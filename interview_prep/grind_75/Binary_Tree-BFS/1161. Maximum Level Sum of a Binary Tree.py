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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        this will be solved with level order traversal
        :param root:
        :return:
        """
        max_sum = float('-inf')
        q = deque([root])
        level = 1
        max_at_level = 1
        while q:
            lenQ = len(q)
            level_sum = 0
            for i in range(lenQ):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_at_level = level
                max_sum = level_sum
            level += 1
        return max_at_level


if __name__ == '__main__':
    sol = Solution()
    root = [989,None,10250,98693,-89388,None,None,None,-32127]
    # root = [1, 7, 0, 7, -8, None, None]
    root = [-100, -200, -300, -20, -5, -10, None]
    root = build_tree(root)
    print(sol.maxLevelSum(root))