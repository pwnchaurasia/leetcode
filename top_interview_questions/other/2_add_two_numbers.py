
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode()
        l3 = head
        carry = 0 
        while l1.next is not None and l2.next is not None:
             s = l1.val + l2.val + carry
             if s > 10:
                carry = s % 10
                val = s//10
                l3.val = val
                l3.next = ListNode()
                l1 = l1.next
                l2 = l2.next
        
        while l1.next is not None:
            s = l1.val + carry
            if s > 10:
                carry = s % 10
                val = s//10
                l3.val = val
                l3.next = ListNode()
                l1 = l1.next
        
        while l2.next is not None:
            s = l2.val + carry
            if s > 10:
                carry = s % 10
                val = s//10
                l3.val = val
                l3.next = ListNode()
                l2 = l2.next




ltr2 = [5,6,4]


ltr = [2,4,3]
head1 = ListNode()
l1 = head1
for i in ltr:
    l1.val = i
    l1.next = ListNode()
    l1 = l1.next


ltr2 = [5,6,4]
head2 = ListNode()
l2 = head2
for i in ltr:
    l2.val = i
    l2.next = ListNode()
    l2 = l2.next






hh = Solution().addTwoNumbers(head1, head2)
while hh is not None:
    print(head1.val)
    head1 = head1.next


# while head1 is not None:
#     print(head1.val)
#     head1 = head1.next