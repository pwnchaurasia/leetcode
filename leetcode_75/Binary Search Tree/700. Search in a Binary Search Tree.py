# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root:
            if root.val == val:
                return root
            elif root.left and root.val > val:
                root = root.left
            elif root.right and root.val < val:
                root = root.right
            else:
                break
        return None
