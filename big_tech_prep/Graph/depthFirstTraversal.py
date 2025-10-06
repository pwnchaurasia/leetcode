

def depth_first_traversal(graph, source):
    stack = [source]

    while stack:
        vertex = stack.pop()
        print(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)


def depth_with_recur(graph, source):
    print(source)
    for i in graph[source]:
        depth_with_recur(graph, i)

if __name__ == '__main__':

    adj = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    depth_first_traversal(adj, 'a')
    print("******"*20)
    depth_with_recur(adj, 'a')