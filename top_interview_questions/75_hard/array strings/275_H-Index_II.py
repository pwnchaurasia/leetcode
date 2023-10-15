"""
Logic: 




"""


from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        N = len(citations)
        for i, v in enumerate(citations):
            if N-i <= v:
                count +=1
        return count
    


citations = [1,2,100]
sol = Solution()
print(sol.hIndex(citations=citations))
