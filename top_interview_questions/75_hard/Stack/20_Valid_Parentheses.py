class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "({["
        brackets_hash = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top_item = stack.pop()
                if brackets_hash[top_item] != i:
                    return False
        return True if len(stack) == 0 else False



s = "()"
sol = Solution()
s = "()[]{}"
s = "(]"
print(sol.isValid(s))