from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxer = 0
        for i in nums:
            length = 0 
            if i-1 not in numSet:
                while i+length in nums:
                    length +=1
                    maxer = max(maxer, length)
        return maxer
    


sol =Solution()
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [0,1,-1,-5,-3]
print(sol.longestConsecutive(nums))