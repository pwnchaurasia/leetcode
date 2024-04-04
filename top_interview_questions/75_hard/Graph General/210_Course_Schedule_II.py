class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to prerequisites list
        pre_req_hash = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req_hash[crs].append(pre)
        
        # a course can have 3 states
        # visited -> course has been added to the output
        # visiting -> course has not visted yet but currently in cycle
        # unvisted -> course not added to output or cycle
        output = []
        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in pre_req_hash[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return output