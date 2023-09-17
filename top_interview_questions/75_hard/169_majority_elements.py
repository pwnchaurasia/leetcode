from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_book = {}
        for x in nums:
            if x in count_book:
                count_book[x] +=1
            else:
                count_book[x] = 1

        max = -9999999999
        val = None
        for item in count_book:
            if count_book[item] > max:
                max = count_book[item]
                val = item
        return val


    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        return nums[mid]



nums = [2,2,1,1,1,2,2]
val = 2
sol = Solution()
print('ans-->', sol.majorityElement(nums))
