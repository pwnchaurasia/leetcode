class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        strs = [i for i in s]
        vowels = 'aeiouAEIOU'
        while start < end:
            if strs[start] in vowels and strs[end] in vowels:
                strs[start], strs[end] = strs[end], strs[start]
                start += 1
                end -= 1
            elif strs[start] in vowels:
                end -=1
            else:
                start += 1
        return "".join(strs)
