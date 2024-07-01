class Solution:
    def reverseWords(self, s: str) -> str:
        revstr = ""
        temp_rev = ""
        for st in s:
            if st == " ":
                revstr = temp_rev.strip() + " " + revstr.strip()
                temp_rev = ""
            else:
                temp_rev += st.strip()
        if temp_rev != "":
            revstr = temp_rev.strip() + " " + revstr.strip()
        return revstr.strip()


sol = Solution()
s = "  hello world  "
s = "a good   example"
print(sol.reverseWords(s=s))
