# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def smallest_descendant(node):
            while node.left:
                node = node.left
            return node

        if not root:
            return
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    temp = smallest_descendant(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
        return root