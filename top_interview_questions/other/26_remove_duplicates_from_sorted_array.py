from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index


    def removeDuplicates_2(self, nums: List[int]) -> int:
        prev = None
        curr_index = 0
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        for i in nums:
            current = i
            if prev is None:
                prev = current
            else:
                if prev == current:
                    nums[curr_index] = "_"
                else:
                    prev = current
            curr_index += 1
        num_found_at = None
        curr_index = 0
        cntr = 0
        for num in nums:
            if num != "_":
                cntr += 1
                if num_found_at is None:
                    nums[0] = num
                    num_found_at = 0
                else:
                    num_found_at += 1
                    nums[num_found_at] = num
                    nums[curr_index] = "_"
            else:
                nums[curr_index] = "_"
            curr_index += 1
        # print("num_found_at", num_found_at, "cntr", cntr)
        return cntr, nums


listt = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4]
# listt = [1, 2]
print(len(listt))
ss = Solution()
print(ss.removeDuplicates(listt))
