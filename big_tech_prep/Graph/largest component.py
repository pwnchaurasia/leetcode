def explore(graph, src, visited):
    if src in visited: return 0
    stack = [src]
    counter = 0
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        counter += 1
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return counter


def largest_component(graph):
    visited = set()
    max_size = 0
    for node in graph:
        cntr = explore(graph=graph, src=node, visited=visited)
        max_size = max(max_size, cntr)
    return max_size




if __name__ == "__main__":
    graph = {
          0: [8, 1, 5],
          1: [0],
          5: [0, 8],
          8: [0, 5],
          2: [3, 4],
          3: [2, 4],
          4: [3, 2]
    }
    print(largest_component(graph=graph))
    graph = {
        1: [2],
        2: [1, 8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]
    }
    print(largest_component(graph=graph))

    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }
    print(largest_component(graph=graph))

    graph = {
          0: [4,7],
          1: [],
          2: [],
          3: [6],
          4: [0],
          6: [3],
          7: [0],
          8: []
        }
    print(largest_component(graph=graph))