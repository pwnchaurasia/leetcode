class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_counter = 0
        t_counter = 0
        res = [False]*len(s)
        while s_counter < len(s):
            char = s[s_counter]
            while t_counter < len(t):
                if char == t[t_counter]:
                    res[s_counter] = True
                    t_counter += 1
                    break
                t_counter += 1
            s_counter += 1
        return all(res)


        # optimized solution

        s_counter = 0
        t_counter = 0
        while s_counter < len(s) and t_counter < len(t):
            char = s[s_counter]
            if char == t[t_counter]:
                s_counter += 1
            t_counter += 1
        return s_counter == len(s)

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s=s, t=t))
    s = "axc"
    t = "ahbgdc"
    print(sol.isSubsequence(s=s, t=t))
