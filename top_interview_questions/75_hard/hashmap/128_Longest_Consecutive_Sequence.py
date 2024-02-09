from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for n in nums:
            if n-1 in nums:
                continue
            nxt=n
            while (nxt+1) in nums:
                nxt+=1
            ans=max(ans,nxt-n+1)
        return ans
    


sol =Solution()
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [0,1,-1,-5,-3]
print(sol.longestConsecutive(nums))