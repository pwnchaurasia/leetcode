from typing import  List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        ops = 0
        while i < j:
            t = nums[i] + nums[j]
            if  t == k:
               ops += 1
               i += 1
               j -= 1
            elif t > k:
                j -= 1
            else:
                i += 1
        return ops


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    k = 5
    res = sol.maxOperations(nums=nums, k=k)
    print(res)

    nums = [3,1,3,4,3]
    k = 6
    res = sol.maxOperations(nums=nums, k=k)
    print(res)