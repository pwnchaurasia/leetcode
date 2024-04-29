from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        val = heapq.nlargest(k, nums)[-1]

        return val