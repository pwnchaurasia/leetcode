

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p1 = 0
        p2 = 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return len(s) == p1


if __name__ == "__main__":
    t = "ahgbgdc"
    s = "abc"

    sol = Solution()
    res = sol.isSubsequence(s, t)
    print(res)

    s = "axc"
    t = "ahbgdc"
    res = sol.isSubsequence(s, t)
    print(res)
