import collections


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = collections.defaultdict(list)

        if not isConnected: return 0

        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False]*n

        def dfs(u):
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)
        count = 0

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count
