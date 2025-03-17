class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        counter = 1
        l = len(s)
        while counter < l:
            ss = s[counter]
            if ss == "*":
                stack.pop()
            else:
                stack.append(ss)
            counter += 1
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = "leet**cod*e"
    res = sol.removeStars(s=s)
    print(res)
