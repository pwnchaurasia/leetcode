# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    val = None

    @classmethod
    def guess(cls, picked):
        if picked > cls.val:
            return -1
        elif picked < cls.val:
            return 1
        else:
            return 0

    @classmethod
    def pick_number(cls, n):
        cls.val = 3

    def guessNumber(self, n: int) -> int:
        Solution.pick_number(n)
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            is_correct = Solution.guess(mid)
            # is_correct = guess(picked)
            if is_correct  == -1:
                right = mid - 1
            elif is_correct == 1:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.guessNumber(n))

