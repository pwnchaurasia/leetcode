# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length+=1
        
        k = k % length
        if k==0:
            return head
        
        cur = head
        for i in range(length-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead

       




# head = [1,1,1,2,3]
arr = [1,2,3,4,5], 
k = 2

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

linked_list_head = create_linked_list(arr)
sol = Solution()
sol.rotateRight(head=linked_list_head, k=k)

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
arr = [1, 2, 3, 4, 5]
linked_list_head = create_linked_list(arr)
print_linked_list(linked_list_head)