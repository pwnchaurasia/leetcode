class Solution:

    def haser(self, st):
        return hash(st)

    def strStr(self, haystack: str, needle:str) -> int:
        if len(needle) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        len_of_need = len(needle)
        len_of_hay = len(haystack)
        hash_of_need = self.haser(needle)
        for i in range(0, len_of_hay, 1):
            cu = haystack[i:i+len_of_need]
            if hash_of_need == self.haser(cu):
                return i
        return -1

    def strStr_not_working(self, haystack: str, needle: str) -> int:
        if (len(needle) == 0):
            return 0
        elif (len(haystack) == 0):
            return -1
        hay_index = 0
        needle_index = 0
        len_needle = len(needle)
        found_at_index = None
        match_started = None
        broke = False
        while hay_index <= (len(haystack)-1):
            if haystack[hay_index] == needle[needle_index]:
                if match_started is None:
                    match_started = hay_index
                if needle_index == (len_needle - 1):
                    found_at_index = hay_index
                    break
                else:
                    broke = True
                needle_index += 1
            else:
                needle_index = 0
                found_at_index = None
                if broke:
                    hay_index = match_started + 1
                    match_started = None
                    broke = False
            hay_index += 1
        if found_at_index is None:
            return -1
        else:
            return (found_at_index - (len_needle-1))


haystack = "mississippi"
needle = "ppi"
ss = Solution()
print(ss.strStr(haystack, needle))
