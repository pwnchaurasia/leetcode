
def explore(adj, src, visited):
    if src in visited: return False
    stack = [src]
    while stack:
        curr = stack.pop()
        visited.add(curr)
        for node in adj[curr]:
            if node not in visited:
                stack.append(node)
    return True



def count_connected_components(adj):
    visited = set()
    counter = 0
    for node in adj:
        is_new = explore(adj=adj, src=node, visited=visited)
        if is_new:
            counter += 1
    return counter



if __name__ == "__main__":
    adj = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    count = count_connected_components(adj=adj)
    print(count)