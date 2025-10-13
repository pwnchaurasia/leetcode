from typing import List

class Solution:

    def explore_depth_wise(self, isConnected, city, visited):
        if city in visited:
            return False
        visited.add(city)

        for nei in range(len(isConnected)):
            if isConnected[city][nei] == 1:
                self.explore_depth_wise(
                    isConnected=isConnected,
                    city=city,
                    visited=visited
                )
        return True


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for city in range(len(isConnected)):
            if self.explore_depth_wise(isConnected=isConnected, city=city, visited=visited)
                count += 1




if __name__ == "__main__":
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    sol.findCircleNum(isConnected=isConnected)
