# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        # with in order traversal
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)


        depth = max(left_depth, right_depth)+1

        return depth