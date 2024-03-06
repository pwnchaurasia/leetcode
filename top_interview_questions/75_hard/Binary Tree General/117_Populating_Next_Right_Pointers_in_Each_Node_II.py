from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        temp = root
        while q:

            poped = q.popleft()
            print(poped.val)
            temp.right = poped
            temp.left = None
            temp = temp.right
            if poped.left:
                q.append(poped.left)
            if poped.right:
                q.append(poped.right)
        return root


        



root =  Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.left = None
root.right.right = Node(7)

sol =Solution()
new_root = sol.connect(root)

result = []
while new_root:
    print(root.val)
    print(root.next)




