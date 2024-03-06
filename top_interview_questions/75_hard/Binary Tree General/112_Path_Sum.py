# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        stack = [(root, root.value)]

        while stack:
            current_node, current_sum = stack.pop()

            if not current_node.left and not current_node.right and current_sum == targetSum:
                return True

            if current_node.right:
                stack.append((current_node.right, current_sum + current_node.right.value))

            if current_node.left:
                stack.append((current_node.left, current_sum + current_node.left.value))

        return False


        