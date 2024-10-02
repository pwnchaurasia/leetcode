# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        length = 0
        hashed = {}
        while head:
            hashed[length] = head.val
            head = head.next
            length += 1

        max_twin = float('-inf')
        for i in range(length):
            twin = length - 1 - i
            value = hashed[twin] + hashed[i]
            max_twin = max(max_twin, value)
        return max_twin


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
    head = [1,100000]
    head = list_to_linked_list(head)

    new_head = sol.pairSum(head=head)
    # print_linked_list(new_head)
    print(new_head)
