class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = ""
        for i in s:
            if i != " ":
                word = word + i
            elif i == " ":
                if word != "":
                    result = (word + " " + result if result != " " else word.strip()).strip()
                    word = ""
        if result != "":
            result = (word + " " + result).strip()
        else:
            result = word.strip()
        return result



if __name__ == '__main__':
    sol = Solution()
    # s = "the sky is blue"
    # print(sol.reverseWords(s=s) == "blue is sky the")
    # s = "EPY2giL"
    # print(sol.reverseWords(s=s) == "EPY2giL")

    s = "  hello world  "
    print(sol.reverseWords(s=s))