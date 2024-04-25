# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(start, end):
            if start > end:
                return None

            m = (start + end) // 2
            root = TreeNode(nums[m])
            root.left = helper(start, m-1)
            root.right = helper(m+1, end)
            return root
        return helper(0, len(nums)-1)