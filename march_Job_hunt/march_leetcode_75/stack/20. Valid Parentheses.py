class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "({["
        stack = []
        braces_hash = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if braces_hash[i] != top:
                    return False
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    s = "(){}[[[(({))]]]"
    res = sol.isValid(s=s)
    print(res)