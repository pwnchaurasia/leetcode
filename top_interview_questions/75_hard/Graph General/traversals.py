adjaceny_graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c':['e'],
    'd': ['f'],
    'e': [],
    'f':[]
}


def depath_first_traversal(node, source):
    stack = []
    stack.append(node)
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        neighbours = source[node]
        for i in neighbours:
            stack.append(i)
    return res



def breadth_first_traversal(node, source_graph):
    import collections
    q = collections.deque([node])
    res = []
    while q:
        lenQ = len(q)
        for i in range(lenQ):
            node = q.popleft()
            res.append(node)
            neighbours = source_graph[node]
            for i in neighbours:
                q.append(i)
    return res




print(depath_first_traversal('a', adjaceny_graph))
print(breadth_first_traversal('a', adjaceny_graph))
