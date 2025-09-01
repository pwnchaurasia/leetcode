"""
it's a two pointer problem,
take p1 for s and p2 for t.
1. loop throw s and t it pointers ar smaller than their length.
2. if chat at p1 and p2 are same, increment p1
3. if not increment p2
4. at last check if p1 is reached till it length

"""



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0,0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 2
        return p1 == len(s)


