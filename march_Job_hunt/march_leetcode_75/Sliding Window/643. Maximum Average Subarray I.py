from typing import  List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_sum = max_sum = sum(nums[:k])

        for inter in range(k, len(nums)):
            leave = nums[inter - k]
            curr_sum = curr_sum - leave + nums[inter]
            max_sum = max(max_sum, curr_sum)

        return max_sum/k



if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    sol = Solution()
    res = sol.findMaxAverage(nums=nums, k=k)
    print(res)

    nums = [0,4,0,3,2]
    k = 1
    sol = Solution()
    res = sol.findMaxAverage(nums=nums, k=k)
    print(res)