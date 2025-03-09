class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Ensure str1 is the shorter one
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        while str2:
            if not str1.startswith(str2):
                return ""
            str1, str2 = str2, str1[len(str2):]
        return str1


if __name__ == "__main__":
    sol = Solution()
    str1 = "ABCABCABC"
    str2 = "ABCABC"
    res = sol.gcdOfStrings(str1=str1, str2=str2)
    print(res)