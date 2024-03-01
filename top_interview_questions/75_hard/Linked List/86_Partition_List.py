# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return head

        small_list = []
        big_list = []
        temp = head
        while head:
            if head.val < x:
                small_list.append(head)
            else:
                big_list.append(head)
            head = head.next

        new_head = None
        temp = None
        l, r = 0, 0
        while l < len(small_list):
            if new_head is None:
                new_head = small_list[l]
                temp = new_head
            else:
                new_head.next = small_list[l]
                new_head = new_head.next
            l+=1
        
        l, r = 0, 0 
        while l < len(big_list):
            if new_head is None:
                new_head = big_list[l]
                temp = new_head
            else:
                new_head.next = big_list[l]
                new_head = new_head.next
            l+=1
        new_head.next = None
        return temp



def create_linked_list(arr):
    if not arr:
        return None
    
    # Create the head of the linked list
    head = ListNode(arr[0])
    current = head

    # Iterate through the rest of the elements to create nodes
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

# Example usage:
# head = [1, 4, 3, 2, 5, 2]
# # head = [2,1]
# x =3
# # x =2

head = [1]
x = 0
linked_list_head = create_linked_list(head)

sol = Solution()
sol_head = sol.partition(linked_list_head, x=x)
print(sol_head)

while sol_head:
    print("ss", sol_head.val)
    sol_head = sol_head.next