from typing import List
class Solution:
    # def compress(self, chars: List[str]) -> int:
        # hashed = {}
        # for char in chars:
        #     hashed[char] = hashed.get(char, 0) + 1
        #
        # # print(hashed)
        # counter = 0
        # result = []
        # for key in hashed:
        #     val = hashed[key]
        #     if val == 1:
        #         result.append(key)
        #     elif val > 10:
        #         result.append(key)
        #         for i in str(val):
        #             result.append(i)
        #     else:
        #         result.append(key)
        #         result.append(str(val))
        # return result
    def compress(self, chars: List[str]) -> int:

        ans = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            char_counter = 0
            while i < len(chars) and chars[i] == char:
                char_counter += 1
                i += 1
            chars[ans] = char
            ans += 1
            if char_counter > 1:
                for c in str(char_counter):
                    chars[ans] = c
                    ans += 1
        return ans




if __name__ == "__main__":
    sol = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(sol.compress(chars=chars))

    # chars = ["a"]
    # print(sol.compress(chars=chars))
    #
    # chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # print(sol.compress(chars=chars))