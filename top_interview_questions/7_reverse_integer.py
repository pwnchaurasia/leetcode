from builtins import int


class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        if "-" in num:
            rest_num = num[1:]
            rest_num = rest_num[::-1]
            rest_num.insert(0, "-")
            num = "".join(rest_num)
        else:
            num = num[::-1]
            num = "".join(num)
        if abs(int(num)) < 2 ** 31 and int(num) != 2**31 - 1:
            return int(num)
        else:
            return 0


x = -1234567899
s = Solution()
print(s.reverse(x))
