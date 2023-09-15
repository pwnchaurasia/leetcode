#logic
'''
take two pointers, L and R,
loop through the list,
increment R till we will find the different number,
keep a counter to count how many duplicates encounterd

no


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0

        while r < len(nums):
            counter = 1
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                counter += 1

            for i in range(min(2, counter)): [1,1,1,1,2,2,2,3,3,3,4,4]
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
