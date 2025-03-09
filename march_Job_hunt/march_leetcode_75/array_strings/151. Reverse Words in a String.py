class Solution:
    def reverseWords(self, s: str) -> str:

        word = ""
        sent = ""
        for i in s:
            if i == " ":
                sent =  word.strip() + " " + sent
                word = ""
                # sent = sent.strip()
            else:
                word += i
        if word != "":
            sent = word.strip() + " " + sent.strip()

        return sent.strip()


if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    re = sol.reverseWords(s=s)
    print(re)

    s = "    hello world      "
    re = sol.reverseWords(s=s)
    print(re)

    s = "EPY2giL"
    re = sol.reverseWords(s=s)
    print(re)