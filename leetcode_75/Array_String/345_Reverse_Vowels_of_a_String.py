class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        while l < r:
            l_val = s[l]
            r_val = s[r]
            print(l_val)
            print(r_val)
            if l_val.lower() in vowels and r_val.lower() in vowels:
                s[l] = r_val
                s[r] = l_val
                l += 1
                r -= 1
            if l_val.lower() not in vowels:
                l += 1
            if r_val.lower() not in vowels:
                r -= 1
        return "".join(s)


sol = Solution()
s = "leetcode"
print(sol.reverseVowels(s=s))



