from typing import List

class Solution:
    def make_adj_list(self, rooms):
        adj_list = {}
        for idx, room in enumerate(rooms):
            for key in room:
                adj_list[idx] = adj_list.get(idx, [])
                adj_list[idx].append(key)
        return adj_list

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # adj = self.make_adj_list(rooms)
        visited = set()
        visited.add(0)
        stack = [0]
        while stack:
            curr = stack.pop()
            for key in rooms[curr]:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)






if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    sol = Solution()
    print(sol.canVisitAllRooms(rooms=rooms))

