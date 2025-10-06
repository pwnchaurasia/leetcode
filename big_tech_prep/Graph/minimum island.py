from collections import deque
def minimum_island(grid):
    visited = set()
    min_size = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            size = explore_depth_wise(grid=grid, r=r, c=c, visited=visited)
            if size:
                min_size = min(min_size, size)
    return min_size



def explore_depth_wise(grid, r, c, visited):
    row_bound = 0 <= r < len(grid)
    col_bound = 0 <= c < len(grid[0])

    if not row_bound or not col_bound: return 0

    if grid[r][c] == "W": return 0

    pos = f"{r},{c}"

    if pos in visited: return 0

    visited.add(pos)

    size = 1
    size += explore_depth_wise(grid=grid, r = r + 1, c = c, visited=visited)
    size += explore_depth_wise(grid=grid, r = r - 1, c = c, visited=visited)
    size += explore_depth_wise(grid=grid, r = r, c = c + 1, visited=visited)
    size += explore_depth_wise(grid=grid, r = r, c = c - 1, visited=visited)

    return size

if __name__ == "__main__":
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(minimum_island(grid=grid))