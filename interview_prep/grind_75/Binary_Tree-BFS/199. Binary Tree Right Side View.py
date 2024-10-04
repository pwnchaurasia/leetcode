# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from collections import deque
from typing import Optional, List

from interview_prep.grind_75.Binary_Tree_DFS.tree_builder import build_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque([root])

        while q:
            right_node = None
            lenQ = len(q)

            for i in range(lenQ):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                res.append(right_node.val)
        return res


if __name__ == '__main__':
    s = Solution()
    root = [1, 2, 3, None, 5, None, 4]
    root = build_tree(root)
    print(s.rightSideView(root))