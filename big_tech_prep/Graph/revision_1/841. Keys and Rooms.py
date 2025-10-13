from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = {}
        visited = set()
        for i in range(len(rooms)):
            adj_list[i] = adj_list.get(i, [])
            adj_list[i].extend(rooms[i])

        stack = []
        stack.append(0)
        visited.add(0)
        while stack:
            curr = stack.pop()
            for key in adj_list[curr]:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)




if __name__ == "__main__":
    sol =  Solution()
    rooms = [[1], [2], [3], []]

    print(sol.canVisitAllRooms(rooms=rooms))
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(sol.canVisitAllRooms(rooms=rooms))
