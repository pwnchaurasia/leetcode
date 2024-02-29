# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        prev = dummy
        while head and head.next:
            if head.val != head.next.val:
                prev = head
                head = head.next
            else:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
                head = head.next
        return dummy.next





# head = [1,1,1,2,3]
head = [1,2,3,3,3,4,4,5]

h = ListNode(head[0])
dummy = h
for i in range(1, len(head)):
    val = ListNode(head[i])
    h.next = val
    h = h.next

# print(dummy.val)

sol = Solution()
new_head = sol.deleteDuplicates(dummy)

while new_head:
    print(new_head.val)
    new_head = new_head.next
