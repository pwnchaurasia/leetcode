from collections import deque
from inspect import stack


class Solution:
    def decodeString(self, s: str) -> str:

        stack = deque()

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                res = ""
                while stack[-1] != "[":
                    res = stack.pop() + res
                stack.pop() # removing [
                n = ""
                while len(stack) != 0 and stack[-1].isdigit():
                    n += stack.pop()
                stack.append(res*int(n[::-1]))
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = "3[a]2[bc]"
    s = "3[a2[c]]"
    s = "2[abc]3[cd]ef"
    re = sol.decodeString(s=s)
    print(re)