class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapper_s = {}
        mapper_t = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 not in mapper_s:
                mapper_s[c1] = 1
            else:
                mapper_s[c1] += 1
            if c2 not in mapper_t:
                mapper_t[c2] = 1
            else:
                mapper_t[c2] += 1
        
        for i in mapper_s:
            if i not in mapper_t or mapper_s[i] != mapper_t[i]:
                return False
        return True

                






sol = Solution()
s = "anagras"
t = "nagaram"
print(sol.isAnagram(s=s, t=t))