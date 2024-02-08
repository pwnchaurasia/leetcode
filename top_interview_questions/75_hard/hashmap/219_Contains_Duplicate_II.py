from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_record = {}
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                index_record.pop(nums[L],None)
                L+=1
                
            if nums[R] in index_record:
                return True
            index_record[nums[R]] = True
        return False







nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums=nums, k=k))