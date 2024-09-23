class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeros +=1
            elif nums[i] == 1:
                ones +=1

        for j in range(n):
            if j < zeros:
                nums[j] = 0
            elif zeros <= j < ones+zeros:
                nums[j] = 1
            else:
                nums[j] = 2



if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(sol.sortColors(nums=nums))

    nums = [0, 1, 0, 2, 0, 1, 2, 0, 2, 1, 1, 0]
    print(sol.sortColors(nums=nums))