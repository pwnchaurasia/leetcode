# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp_list = []
        # curr = head
        # while curr is not None:
        #     temp_list.append(curr.val)
        #     curr = curr.next
        # temp_list.sort()
        #
        # curr = head
        # while curr is not None:
        #     curr.val = temp_list.pop(0)
        #     curr = curr.next
        # return head

        if not head and not head.next:
            return head

        left = head
        right = self.get_mid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
