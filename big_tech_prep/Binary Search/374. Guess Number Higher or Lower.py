# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    gg = 6
    if num == gg:
        return 0
    elif num > gg:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right-left)//2
            guessed_num = guess(mid)
            if guessed_num == 0:
                return mid
            elif guessed_num == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1


sol = Solution()
n = 10
pick = 6
print(sol.guessNumber(n=n))