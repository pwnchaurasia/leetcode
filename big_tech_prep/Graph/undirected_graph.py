
def buildGraph(edges):
    adj_list = {}
    for a, b in edges:
        adj_list[a] = adj_list.get(a, [])
        adj_list[b] = adj_list.get(b, [])
        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list

def has_path(adj_list, src, dest):
    visited = set()
    if src == dest: return True
    stack = [src]
    while stack:
        curr = stack.pop()
        visited.add(curr)
        if curr == dest: return True
        for neighbor in adj_list[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

def undirect_graph(edges, src, dest):
    adj_list = buildGraph(edges)
    return has_path(adj_list=adj_list, src=src, dest=dest)

if __name__ == "__main__":
    edges = [
        ['i','j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    undirect_graph(edges, 'i', 'j')