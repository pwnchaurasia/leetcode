# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        import collections
        res = []
        q = collections.deque([root])

        while q:
            lenQ = len(q)
            vals = 0
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    vals += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(vals/lenQ)
        return res