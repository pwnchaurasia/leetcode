class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



def insert_into_ll(head, val, match_val):

    new_node = ListNode(val)
    curr = head
    while curr:
        if curr.val == match_val:
            cur_next = curr.next
            curr.next = new_node
            new_node.next = cur_next
            break
        curr = curr.next
    return head



l0 = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)


l0.next = l1
l1.next = l2
l2.next = l4
l4.next = l5

# while l0:
#     print(l0.val)
#     l0 = l0.next
#
# print("**"*12)


he = insert_into_ll(l0, 3, 2)

while he:
    print(he.val)
    he = he.next


