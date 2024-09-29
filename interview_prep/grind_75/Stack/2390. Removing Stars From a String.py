class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 0: return ''
        stack = []
        res = ""
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    stack.pop()
        return "".join(stack)




if __name__ == '__main__':
    sol = Solution()
    s = "leet**cod*e"
    s = "erase*****"
    print(sol.removeStars(s=s))