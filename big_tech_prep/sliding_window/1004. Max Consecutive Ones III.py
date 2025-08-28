from typing import List

"""
when u encounter 0 decrement k
when k become less than 0
keep on checking if the leaving digit is 0
if its 0 increment k
and increment left 

length will be right - left + 1
+1 is there because array is zero indexing.
Without the +1, you’d just get the distance between indices, 
not the count of elements in the window.


"""



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1