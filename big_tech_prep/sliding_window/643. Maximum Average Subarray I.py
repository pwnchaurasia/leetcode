from typing import List

"""
first find the max sum and max sum in k
loop through the rest of the numbers

find the leaving number
from the sum_in_k subtract the leaving number and then add the incoming number
then use this to find out max_sum

to get the average sum_in_k/k to get the average

"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_in_k, max_sum = sum(nums[:k])

        for right in range(k, len(nums)):
            leave = nums[right -k]
            sum_in_k = sum_in_k - leave + nums[right]
            max_sum = max(max_sum, sum_in_k)
        return sum_in_k/k