from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2
        new_ll = ListNode(0)
        temp = new_ll
        while l1_head is not None and l2_head is not None:
            if l1_head.val <= l2_head.val:
                temp.next = ListNode(l1_head.val)
                temp = temp.next
                l1_head = l1_head.next
            else:
                temp.next = ListNode(l2_head.val)
                temp = temp.next
                l2_head = l2_head.next

        if l1_head == None:
            while l2_head is not None:
                temp.next = ListNode(l2_head.val)
                temp = temp.next
                l2_head = l2_head.next
        if l2_head == None:
            while l1_head is not None:
                temp.next = ListNode(l1_head.val)
                temp = temp.next
                l1_head = l1_head.next
        return new_ll.next


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_1.next = l1_2
l1_3 = ListNode(4)
l1_2.next = l1_3
# l1_4 = ListNode(141)
# l1_3.next = l1_4
# l1_5 = ListNode(521)
# l1_4.next = l1_5

print("************")
l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_1.next = l2_2
l2_3 = ListNode(4)
l2_2.next = l2_3
# l2_4 = ListNode(464)
# l2_3.next = l2_4
# l2_5 = ListNode(455)
# l2_4.next = l2_5

ss = Solution()
lll = ss.mergeTwoLists(l1_1, l2_1)
while lll.next is not None:
    print(lll.val)
    lll = lll.next

