class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



def delete_give_node_from_ll(head, val):

    curr = head
    prev = None
    while curr:
        if curr.val == val:
            if not prev:
                return curr.next
            else:
                next_node = curr.next
                prev.next = next_node
                break
        else:
            prev = curr
            curr = curr.next
    return head