class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr_value = sum([1 for i in s[:k] if i.lower() in vowels])
        max_value = curr_value
        for i in range(k, len(s)):
            leaving_char = s[i-k].lower()
            adding_char = s[i].lower()
            if leaving_char in vowels:
                curr_value -= 1
            if adding_char in vowels:
                curr_value += 1
            max_value = max(curr_value, max_value)
        return max_value



if __name__ == "__main__":
    sol = Solution()

    s = "abciiidef"
    k = 3

    print(sol.maxVowels(s=s, k=k) == 3)

    s = "aeiou"
    k = 2

    print(sol.maxVowels(s=s, k=k) == 2)

    s = "leetcode"
    k = 3

    print(sol.maxVowels(s=s,k=k) == 2)