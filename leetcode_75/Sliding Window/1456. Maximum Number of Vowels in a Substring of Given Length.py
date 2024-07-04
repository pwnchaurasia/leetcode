class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = list(s)
        subs = s[0:k]
        vowel_count = sum(1 for i in subs if i.lower() in 'aeiou')
        max_count = vowel_count
        for i in range(k, len(s)):
            remove = s[i-k]
            if remove in 'aeiou':
                vowel_count -=1
            if s[i] in 'aeiou':
                vowel_count +=1
            max_count = max(max_count, vowel_count)

        return max_count

sol = Solution()
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k))