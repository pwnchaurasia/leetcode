class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None




def middle_of_ll(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
