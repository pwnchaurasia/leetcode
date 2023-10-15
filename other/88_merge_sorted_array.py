from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # mid_1 = -m
        # from_end_1 = - 1
        # ind_2 = - 1

        # while abs(mid_1) <= len(nums1) and abs(ind_2) <= len(nums2):
        #     if nums1[mid_1] < nums2[ind_2]:
        #         nums1[from_end_1] = nums2[ind_2]
        #         from_end_1 -= 1
        #         ind_2 -= 1
        #     else:
        #         nums1[from_end_1] = nums1[mid_1]
        #         from_end_1 -= 1
        #         mid_1 -= 1
        # return nums1

        # merged_list = []
        # counter_m = 0
        # counter_n = 0
        # while True and counter_m != len(nums1) and counter_n != len(nums2):
        #     if nums1[counter_m] > nums2[counter_n]:
        #         if nums2[counter_n] != 0:
        #             merged_list.append(nums2[counter_n])
        #         counter_n += 1
        #     else:
        #         if nums1[counter_m] != 0:
        #             merged_list.append(nums1[counter_m])
        #         counter_m += 1
        #
        # if counter_m != len(nums1):
        #     for i in range(counter_m, len(nums1)):
        #         merged_list.append(nums1[i])
        #
        # if counter_n != len(nums2):
        #     for i in range(counter_n, len(nums2)):
        #         merged_list.append(nums2[i])
        # nums1 = merged_list
        # print(nums1)

        # 3 Pointer solution
        i,j,k = m-1, n-1, m+n-1
        while j >=0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        print(nums1)




nums1 =[1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


if __name__ == "__main__":
    ss = Solution()
    print(ss.merge(nums1, m, nums2, n))
