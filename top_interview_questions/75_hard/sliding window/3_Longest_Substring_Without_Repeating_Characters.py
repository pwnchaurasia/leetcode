class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        charSet = set()
        left = 0

        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxlen = max(maxlen, right - left +1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left +=1
                charSet.add(s[right])
        return maxlen








s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s=s))