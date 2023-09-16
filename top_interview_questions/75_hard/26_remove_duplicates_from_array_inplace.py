from typing import List
'''
Logic:

[0,0,0,1,1,1,1,1,2,2,3,4,4,5]

take two pointers l and r initialise with zero and,
if l and r is same remove the item at r go to next item and when u find any thing
unique fill it in l+1 position





'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0,1
        while r < len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                nums[l+1] = nums[r]
                l+=1
                r+=1
        print(nums)
        return l+1



nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
