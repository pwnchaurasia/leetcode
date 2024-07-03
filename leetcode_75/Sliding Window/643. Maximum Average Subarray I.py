from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]
            maxSum = max(currSum, maxSum)
        return maxSum/k


sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
# nums= [0,1,1,3,3]
# k = 4
nums = [0,4,0,3,2]
k = 1
print(sol.findMaxAverage(nums=nums, k=k))