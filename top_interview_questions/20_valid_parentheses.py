class Solution:

    def match(self, p1, p2):
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        open = "([{"
        i = 0
        open_close = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        while i < len(s) and valid:
            if s[i] in open:
                stack.insert(0, s[i])
            else:
                if stack == []:
                    valid = False
                else:
                    cur = stack.pop(0)
                    if cur != open_close[s[i]]:
                        valid = False
            i += 1
        if len(stack) == 0 and valid:
            return True
        else:
            return False


s = "(){"
string = Solution()
print(string.isValid(s))
