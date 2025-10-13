from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]],
                     values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        for idx, val in enumerate(equations):
            i, j = val
            adj_list[f"{i}"] = adj_list.get(f"{i}", [])
            adj_list[f"{j}"] = adj_list.get(f"{j}", [])
            adj_list[f"{i}"].append((j, values[idx]))
            adj_list[f"{j}"].append((i, 1/values[idx]))

        def bfs(start, end):
            if start not in adj_list or end not in adj_list:
                return -1.0

            q = deque()
            q.append([start, 1.0])
            visited = set()
            visited.add(start)
            while q:
                node, product = q.popleft()
                if node == end:
                    return product

                for nei, val in adj_list[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append([nei, product*val])
            return -1.0

        result = []
        for start, end in queries:
            result.append(bfs(start, end))
        return result






if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"],["a", "a"], ["x", "x"]]

    sol = Solution()
    res = sol.calcEquation(
        equations=equations,
        values=values,
        queries=queries
    )
    print(res)





