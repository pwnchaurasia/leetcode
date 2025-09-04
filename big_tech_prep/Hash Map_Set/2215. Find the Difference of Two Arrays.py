from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_hash = {i: True for i in nums1}
        nums2_hash = {i: True for i in nums2}

        ans = [0,0]
        l1 = []

        for i in nums1_hash:
            if i not in nums2_hash:
                l1.append(i)
        ans[0] = l1
        l2 = []
        for i in nums2_hash:
            if i not in nums1_hash:
                l2.append(i)
        ans[1] = l2
        return ans

        # other way to solve this
        # s1, s2 = set(nums1), set(nums2)
        # return [list(s1 - s2), list(s2 - s1)]



sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(sol.findDifference(nums1=nums1, nums2=nums2))