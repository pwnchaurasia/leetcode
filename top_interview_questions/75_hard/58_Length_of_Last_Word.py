from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [ i.strip() for i in s.split(" ") if i != ""]

        last = words[-1].strip()
        return len(last)
        