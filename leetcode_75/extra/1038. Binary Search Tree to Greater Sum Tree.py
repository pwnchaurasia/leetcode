# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        all_values = []
        large_dict = {}

        def dfs(node):
            if node:
                all_values.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        all_values.sort()
        for i in range(len(all_values)):
            large_dict[all_values[i]] = all_values[i+1:]

        def sum_tree(node):
            if node:
                s = sum(large_dict[node.val])
                node.val = node.val + s
                sum_tree(node.left)
                sum_tree(node.right)

        sum_tree(root)
        return root





root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)

s = Solution()
rr = s.bstToGst(root)


def level_order_traversal(root):
    import collections
    if not root:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

print(level_order_traversal(rr))