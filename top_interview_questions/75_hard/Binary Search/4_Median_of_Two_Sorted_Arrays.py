class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1) - 1
        n = len(nums2) - 1
        new = []
        i, j = 0, 0
        while i <= m and j <= n:
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i = i + 1
            else:
                new.append(nums2[j])
                j = j + 1
        while (i <= m):
            new.append(nums1[i])
            i = i + 1
        while (j <= n):
            new.append(nums2[j])
            j = j + 1
        median = len(new)
        i = median // 2
        if median % 2 == 0:
            median = (new[i - 1] + new[i]) / 2
        else:
            median = new[i]
        return median