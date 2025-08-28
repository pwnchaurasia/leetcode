
"""
s = "abciiidef"
k = 3

This question will be solved using sliding window.

first_count initial vowel count in range k
then loop through k to s
keep on checking each char
first check the leaving char,
if leaving char is in vowels then decrement vowel count
if incoming char is in vowels then increment vowel count

and then set the max_count

answer will be max_count
"""




class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        v_count = sum(1 for c in s[:k] if c in vowels)
        max_count = v_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                v_count -= 1
            if s[i] in vowels:
                v_count += 1
            max_count = max(max_count, v_count)

        return max_count


