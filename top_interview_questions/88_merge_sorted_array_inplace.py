'''
    Logic:
    1. Instead of arranging from start, fill numbers from back side as we know
    list is already sorted.
    [1,2,3,0,0,0]
    [2,5,6]

    i = 0, p1 = 2, p2 =- 1, p3 = -1
    6>3, [1,2,3,0,0,6], p1 =2,  p2 =-2, p3 = -2
    5>3, [1,2,3,0,5,6], p1 =2,  p2 =-3, p3 = -3
    2>3, [1,2,0,3,5,6], p1 =1,  p2 =-3, p3 = -4
    2>0, [1,2,2,3,5,6], p1 =0,  p2 =-4, p3 = -5

'''



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
            else:
                nums1[last] = nums2[n-1]
                n -=1
            last -=1

        while n > 0:
            nums1[last] = nums2[n]
            last -=1
            n -= 1
