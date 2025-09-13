from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and char == chars[read]:
                read += 1
                count += 1

            chars[write] = char
            write += 1
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        return write


sol = Solution()
chars = ["a","a","b","b","c","c","c"]
print(sol.compress(chars=chars))
