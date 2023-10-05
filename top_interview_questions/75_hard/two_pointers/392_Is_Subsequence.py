class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_ptr = 0
        t_ptr = 0
        found = ""
        while s_ptr < len(s) and t_ptr < len(t):
            
            if t[t_ptr] != s[s_ptr]:
                t_ptr +=1
            else:
                found += s[s_ptr]
                s_ptr +=1
                t_ptr +=1
        
        if s == found:
            return True
        return False



s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s=s, t=t))

