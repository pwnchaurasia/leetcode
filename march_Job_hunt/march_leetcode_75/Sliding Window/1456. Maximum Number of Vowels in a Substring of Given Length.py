class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s = [i.lower() for i in s]

        vowel_count = sum(1 for i in s[0:k] if  i in 'aeiou')
        max_count = vowel_count
        for inter in range(k, len(s)):
            char_at = s[inter]
            remove = s[inter-k]

            if remove in 'aeiou':
                vowel_count -= 1
            if char_at in 'aeiou':
                vowel_count += 1
            max_count = max(max_count, vowel_count)
        return max_count



if __name__ == "__main__":
    sol = Solution()
    s = "abciiidef"
    k = 3
    res = sol.maxVowels(s=s, k=k)
    print(res)

