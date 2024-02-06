class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper_s = {}
        mapper_t = {}
        words = s.split(" ")
        if len(pattern) < len(words):
            return False
        for i in range(len(pattern)):
            c1 = pattern[i]
            c2 = words[i]
            if c1 in mapper_s and mapper_s[c1] != c2:
                return False
            if c2 in mapper_t and mapper_t[c2] != c1:
                return False
            
            mapper_s[c1] = c2
            mapper_t[c2] = c1
        return True




sol = Solution()
pattern = "abba"
s = "dog cat caw dog"
print(sol.wordPattern(pattern=pattern, s=s))