# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from tree import list_to_tree
from typing import Optional
class Solution:



    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_nodes(root, arr):
            if not root:
                return
            if root.left is None and root.right is None:
                arr.append(root.val)
            else:
                get_leaf_nodes(root.left, arr)
                get_leaf_nodes(root.right, arr)

        if not root1 or not root2:
            pass
        a1 = []
        a2 = []

        get_leaf_nodes(root=root1, arr=a1)
        get_leaf_nodes(root=root2, arr=a2)

        return a1 == a2


sol = Solution()
root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

root1 = list_to_tree(root1)
root2 = list_to_tree(root2)
sol.leafSimilar(root1=root1, root2=root2)