class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        import collections
        lookup = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            lookup[x][y] = value
            lookup[y][x] = 1.0 / value

        def dfs(x, y, visit):
            if x not in lookup and y not in lookup: return -1
            if y in lookup[x]: return lookup[x][y]

            for i in lookup[x]:
                if i in visit: continue
                visit.add(i)
                temp = dfs(i, y, visit=visit)
                if temp == -1:
                    continue
                else:
                    return lookup[x][i] * temp
            return -1

        res = []
        for x, y in queries:
            res.append(dfs(x, y, set()))