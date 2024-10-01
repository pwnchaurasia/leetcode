# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        temp = head
        odd = head
        even = head.next
        even_start = even

        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_start
        return temp

def list_to_linked_list(lst):
    if not lst:
        return None

    # Create the head of the linked list
    head = ListNode(lst[0])
    current = head

    # Loop through the rest of the list and create nodes
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == '__main__':

    sol = Solution()
    head = [1,2,3,4,5,6,7,8]
    head = list_to_linked_list(head)

    new_head = sol.oddEvenList(head=head)
    print_linked_list(new_head)
