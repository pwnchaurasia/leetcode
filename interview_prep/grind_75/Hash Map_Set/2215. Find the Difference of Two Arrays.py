from typing import List

"""
Appraoch:

take a set of n1 and n2,
because lookup in set is of O(1)
now loop on each set to find out ifs present in other set.
"""




class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = [[], []]

        for i in set1:
            if i not in set2:
                ans[0].append(i)

        for i in set2:
            if i not in set1:
                ans[1].append(i)
        return ans


if __name__ == '__main__':
    sol = Solution()

    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(sol.findDifference(nums1=nums1, nums2=nums2))

    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(sol.findDifference(nums1=nums1, nums2=nums2))