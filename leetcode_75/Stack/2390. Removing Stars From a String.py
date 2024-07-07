from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        stack.append(s[0])
        counter = 1
        l = len(s)
        while counter < l:
            ss = s[counter]
            if ss == "*":
                stack.pop()
            else:
                print(stack)
                stack.append(ss)
            counter += 1
        return "".join(stack)


sol = Solution()
s = "leet**cod*e"
s = "u*ensso****x*q"
print(sol.removeStars(s=s))

