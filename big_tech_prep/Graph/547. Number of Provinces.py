from typing import List

class Solution:
    def explore_depth_wise(self, isConnected, city, visited):
        if city in visited: return False
        visited.add(city)

        for neigh in range(len(isConnected)):
            if isConnected[city][neigh] == 1:
                self.explore_depth_wise(
                    isConnected=isConnected,
                    city=neigh,
                    visited=visited
                )

        return True

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for city in range(len(isConnected)):
            if self.explore_depth_wise(isConnected=isConnected, city=city, visited=visited):
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(sol.findCircleNum(isConnected=isConnected))