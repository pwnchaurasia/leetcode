class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None




def odd_even_ll(head):
    if not head or not head.next:
        return head


    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


