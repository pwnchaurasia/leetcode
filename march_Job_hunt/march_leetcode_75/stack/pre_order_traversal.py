def preorderTraversal(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:  # Right child pushed first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
