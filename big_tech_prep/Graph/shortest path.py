from collections import deque
"""
need to find the shortest path between A and B

to find the shortest path we can do
"""


def adjacency_list(edges):
    adj_list = {}
    for a, b in edges:
        adj_list[a] = adj_list.get(a, [])
        adj_list[b] = adj_list.get(b, [])
        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list

def explore_breadth_first(graph, src, dest, visited):
    q = deque()
    q.append([src, 0])
    visited.add(src)

    while q:
        curr, distance = q.popleft()
        if curr == dest:
            return distance
        for node in graph[curr]:
            if node not in visited:
                visited.add(node)
                q.append([node, distance + 1])
    return -1

def shortest_path(edges, node_A, node_B):
    visited = set()
    adj_list = adjacency_list(edges)
    return explore_breadth_first(adj_list, src=node_A, dest=node_B, visited=visited)



if __name__ == "__main__":
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    print(shortest_path(edges, 'w', 'z'))

    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    val = shortest_path(edges, 'y', 'x') # -> 1
    print(val)

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]

    val2 = shortest_path(edges, 'a', 'e')  # -> 3
    print(val2)