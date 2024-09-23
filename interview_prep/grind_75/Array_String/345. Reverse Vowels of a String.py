class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if s[left] in 'aeiouAEIOU' and s[right] in 'aeiouAEIOU':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            if s[left] not in 'aeiouAEIOU':
                left += 1
            if s[right] not in 'aeiouAEIOU':
                right -= 1
        return "".join(s)

if __name__ == '__main__':
    sol = Solution()
    s = "IceCreAm"
    print(sol.reverseVowels(s=s) == "AceCreIm")


    s = "leetcode"
    print(sol.reverseVowels(s=s) == "leotcede")

