class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



def has_cycle_in_ll(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False



def detect_cycle_and_remove_it(head):
    slow = head
    fast = head
    slow_prev = None
    is_cyclic = False
    while fast and fast.next:
        slow_prev = slow
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            is_cyclic = True
            break

    if not is_cyclic:
        return

    slow = head
    pre = None

    while slow != fast:
        pre = fast
        fast = fast.next
        slow = slow.next
    pre.next = None
    return head


