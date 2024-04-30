class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0:
            digit_sum = carry

            if i >= 0:
                digit_sum += int(a[i])
                i -= 1
            if j >= 0:
                digit_sum += int(b[j])
                j -= 1

            result = str(digit_sum % 2) + result

            carry = digit_sum // 2

        if carry:
            result = "1" + result
        return result
