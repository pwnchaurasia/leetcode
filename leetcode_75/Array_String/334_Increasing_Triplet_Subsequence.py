from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

if __name__ == "__main__":

    sol = Solution()
    nums = [1,2,3,4,5]
    nums = [5,4,3,2,1]
    # nums = [2,1,5,0,4,6]
    nums = [20,100,10,12,5,13]
    print(sol.increasingTriplet(nums=nums))