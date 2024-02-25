from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
            1. sorted array
            2. two pointer start from a number till we find a break or it ends.
            3. store  the first pointer and till before you found the break.
            4. put it in a result array.
        '''
        if nums == []:
            return []

        start_num = nums[0]
        end_num = nums[0]
        res = []
        for num in nums[1:]:
            if num == end_num+1:
                end_num = num
            else:
                if start_num == end_num:
                    res.append(f"{start_num}")
                else:
                    res.append(f"{start_num}->{end_num}")
                start_num = num
                end_num = num

        if start_num == end_num:
            res.append(f"{start_num}")
        else:
            res.append(f"{start_num}->{end_num}")
        return res            


sol = Solution()
nums = [0,2,3,4,6,8,9]
print(sol.summaryRanges(nums=nums))