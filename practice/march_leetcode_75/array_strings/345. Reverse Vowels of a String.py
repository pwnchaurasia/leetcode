class Solution:
    def reverseVowels(self, s: str) -> str:

        start = 0
        end = len(s) - 1
        s = [i for i in s]
        while start < end:
            if s[start] in 'aeiouAEIOU' and s[end] in 'aeiouAEIOU':
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            if s[start] not in 'aeiouAEIOU':
                start += 1
            if s[end] not in 'aeiouAEIOU':
                end -= 1
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    s = "IceCreAm"
    res = sol.reverseVowels(s)
    print(res)

