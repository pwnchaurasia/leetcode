from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i, 0) + 1

        return len(hash_map.values()) == len(set(hash_map.values()))


sol = Solution()
arr = [1,2,2,1,1,3]
arr = [1,2]
print(sol.uniqueOccurrences(arr))