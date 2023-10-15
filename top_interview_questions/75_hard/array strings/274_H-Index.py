from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        count = 0

        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                count+=1
        return count




citations = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex(citations=citations))