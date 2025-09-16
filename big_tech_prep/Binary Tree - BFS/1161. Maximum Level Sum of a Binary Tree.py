from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        leve_max = {}
        queue = deque([root])
        curr_level = 1
        while queue:
            size = len(queue)
            level_sum = 0

            for _ in range(size):
                node = queue.popleft()   # pop from front
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            leve_max[curr_level] = level_sum
            curr_level += 1

        return max(leve_max, key=lambda x: (leve_max[x], -x))
