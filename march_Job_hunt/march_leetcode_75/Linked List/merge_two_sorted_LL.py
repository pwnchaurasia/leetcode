class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None




def merge_two_sorted_ll(head1, head2):
    dummy = ListNode(None)
    curr = dummy
    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    curr.next = head1 if head1 else head2
    return dummy.next