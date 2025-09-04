from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move pointers
            prev = first
            head = first.next
        return dummy.next
