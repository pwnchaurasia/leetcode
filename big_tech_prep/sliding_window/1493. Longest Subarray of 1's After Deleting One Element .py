"""
it's a sliding window problem
initialize left zero and max_count
loop through number
keep checking if its zero
if its zero increment the zero count

as soon zero_count becomes greater than 1
need to release digits from left side
if leaving number is zero
decrement the zero_count
increase left count

and then find the max value
right - left will tell u the length
left will be at the first number 1 and right
will be at the last number 1


"""
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left+=1
            max_count = max(max_count, right - left)
        return max_count

