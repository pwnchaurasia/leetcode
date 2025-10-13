from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj_list = {}
        for i, j in paths:
            adj_list[i] = adj_list.get(i, [])
            adj_list[j] = adj_list.get(j, [])
            adj_list[i].append(j)
            adj_list[j].append(i)

        ans = [0] * n

        for garden in range(1, n+1):
            used_colors = set()
            if garden in adj_list:
                for nei in adj_list[garden]:
                    if ans[nei-1] != 0:
                        used_colors.add(ans[nei-1])

            for color in range(1, 5):
                if color not in used_colors:
                    ans[garden-1] = color
        return ans
