from builtins import str
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        word = min(strs, key=lambda x: len(x))
        rest_word = strs
        i = 0
        pref = ""
        for char in word:
            flag = False
            for wor in rest_word:
                try:
                    if char == wor[i]:
                        flag = True
                    else:
                        flag = False
                        break
                except:
                    flag = False
                    break
            if flag:
                i += 1
                pref += char
            else:
                break
        return pref


strs = ["reflower", "flowe", "floweight"]
strs = ["aaa", "aa", "aaa"]
strs = ["car", "cir"]
s = Solution()
# print(s.longestCommonPrefix(strs))

print(s.sol_2(strs))
