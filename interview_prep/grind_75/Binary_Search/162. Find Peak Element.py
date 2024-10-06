class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If the middle element is greater than the next element,
            # the peak lies on the left (including mid itself).
            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak is in the left half or mid itself
            else:
                left = mid + 1  # Peak is in the right half

        # After the loop, left == right, which points to the peak element.
        return left
