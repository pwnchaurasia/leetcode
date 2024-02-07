from typing import List
import string
from collections import defaultdict
class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] +=1
            print(count)    
            res[tuple(count)].append(s)
        return res.values()

        



sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
strs= ["ac","c"]
strs = ["ac","d"]
print(sol.groupAnagrams(strs))

        
a = 1
b = 2
c = 3
d = 4