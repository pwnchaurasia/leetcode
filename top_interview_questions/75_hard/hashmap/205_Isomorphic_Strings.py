class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapper_s = {}
        mapper_t = {}
        
        for i in range(len(s)):
            
            c1 = s[i]
            c2 = t[i] 
            # print(c1 in mapper_s)
            if c1 in mapper_s and mapper_s[c1] != c2:
                return False
            if c2 in mapper_t and mapper_t[c2] != c1:
                return False
            
            mapper_s[c1] = c2
            mapper_t[c2] = c1
        return True
    

sol = Solution()
s = "egg"
t = "add"

s = "foo"
t = "bar"
print(sol.isIsomorphic(s=s, t=t))

