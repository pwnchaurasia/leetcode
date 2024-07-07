from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c!= "]":
                stack.append(c)
            else:
                res = ''
                while stack[-1] != "[":
                    res += stack.pop()
                stack.pop()  # to pop "["
                n = ''
                while len(stack) !=0 and stack[-1].isdigit():
                    n += stack.pop()
                stack.append(res*int(n[::-1]))
        return ''.join([word[::-1] for word in stack])




sol = Solution()
s = "3[a]2[bc]"
s = "3[a2[c]]"
print(sol.decodeString(s=s))