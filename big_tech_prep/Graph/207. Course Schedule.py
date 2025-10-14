from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        adj = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[b].append(a)

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(sol.canFinish(numCourses=numCourses, prerequisites=prerequisites))
