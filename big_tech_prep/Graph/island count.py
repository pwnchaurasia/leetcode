def island_count(grid):
    visited = set()
    counter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if explore_depth_wise(grid=grid, r=r, c=c, visited=visited):
                counter += 1
    return counter


def explore_depth_wise(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    if not row_inbound or not col_inbound: return False
    if grid[r][c] == "W": return False
    pos = f"{r},{c}"
    if pos in visited: return False
    visited.add(pos)

    explore_depth_wise(grid=grid, r=r - 1, c=c, visited=visited)
    explore_depth_wise(grid=grid, r=r + 1, c=c, visited=visited)
    explore_depth_wise(grid=grid, r=r, c=c - 1, visited=visited)
    explore_depth_wise(grid=grid, r=r, c=c + 1, visited=visited)

    return True





if __name__ == "__main__":
    grid = [
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
    ]
    print(island_count(grid))