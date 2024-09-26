from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        counter = 0

        while start < end:

            if nums[start] + nums[end] > k:
                end -= 1
            elif nums[start] + nums[end] == k:
                start += 1
                end -= 1
                counter += 1
            elif nums[start] + nums[end] < k:
                start +=1
        return counter




if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 2, 3, 4]
    # k = 5
    #
    # print(sol.maxOperations(nums=nums, k=k))
    #
    # nums = [4,4, 1, 3, 1, 3 , 2, 2, 5, 5, 1, 5,2,1,2,3,5,4]
    # k = 2
    #
    # print(sol.maxOperations(nums=nums, k=k))

    nums = [3, 1, 3, 4, 3] # [1,3,3,4]
    k = 6

    print(sol.maxOperations(nums=nums, k=k))