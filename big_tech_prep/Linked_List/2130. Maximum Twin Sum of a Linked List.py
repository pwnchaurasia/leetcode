# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hash_map = {}
        counter  = 0
        while head:
            hash_map[counter] = head.val
            head = head.next
            counter += 1

        max_sum = float('-inf')
        for i in range(counter//2):
            twin_index = counter - 1 - i
            max_sum = max(hash_map[i] + hash_map[twin_index], max_sum)
        return max_sum


sol = Solution()
print(sol.pairSum())

