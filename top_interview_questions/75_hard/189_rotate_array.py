'''
    Logic: 1
    make one extra list then use (i+k)% len(nums) to fill up the result array
    then copy the values to nums array

    Logic 2:

    1. reverse the full list
    2. reverse the fist k element
    3. reverse the k+1 to last element

'''


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length_of_nums = len(nums)
        result = [0]*length_of_nums
        for i in range(length_of_nums):
            index = (i+k)%length_of_nums
            result[index] = nums[i]

        for i in range(length_of_nums):
            nums[i] = result[i]
        return nums

    def rotate2(self, nums: List[int], k: int) -> None:
        # reverse full array
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1
        # reverse first portion now, till k
        l = 0
        r = k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1
        # reverse second portion of list now,
        l = k
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1

        print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
# print(sol.rotate(nums, k))
print(sol.rotate2(nums, k))
