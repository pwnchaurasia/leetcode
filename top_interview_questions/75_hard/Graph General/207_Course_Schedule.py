class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prerequisites list
        pre_req_hash = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req_hash[crs].append(pre)
        # have a visitedSet all courses along the curr DFS path
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if pre_req_hash[crs] == []:
                return True
            visited.add(crs)

            for pre in pre_req_hash[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            pre_req_hash[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True