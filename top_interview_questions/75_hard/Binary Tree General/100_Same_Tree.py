# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def exists_and_have_value(node):
        if not node:
            return False, None
        else:
            return True, node.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            if q is None and p is None:
                 return True
            
            if q is None and p is not None or p is None and q is not None:
                 return False
            
            if p.val != q.val:
                 return False
            
            return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)