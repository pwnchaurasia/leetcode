# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        #delete
        left.next = left.next.next
        return dummy.next




head = [1,2,3,4,5]
n = 2
h = ListNode(head[0])
dummy = h
for i in range(1, len(head)):
    val = ListNode(head[i])
    h.next = val
    h = h.next

# print(dummy.val)

sol = Solution()
print(sol.removeNthFromEnd(dummy, n))
