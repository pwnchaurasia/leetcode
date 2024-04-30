class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        original = x

        while x > 0:
            digit = x % 10
            reverse = (reverse * 10) + digit
            x //= 10
        return reverse == original
