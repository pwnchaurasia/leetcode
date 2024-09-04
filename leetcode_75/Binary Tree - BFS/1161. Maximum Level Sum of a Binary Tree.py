# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        import collections

        q = collections.deque([root])
        maxi = float('-inf')
        level = 1
        min_level = 1

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

            if level_sum > maxi:
                max_sum = level_sum
                min_level = level
            level += 1
        return min_level
