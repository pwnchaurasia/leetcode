
class Solution:
    def firstMissingPositive(self, nums):
        smallest_integer = 1
        nums = list(set(nums))
        for i in nums:
            if i >= 1 and smallest_integer >= i:
                smallest_integer += 1
        return smallest_integer


# nums = [7, 8, 9, 11, 12]
# nums = [1, 2, 0]
nums = [3, 4, -1, 1]
a = Solution()
print(a.firstMissingPositive(nums))
