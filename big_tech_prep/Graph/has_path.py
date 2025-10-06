from collections import deque


## with depth first traversal
def has_path(adj, source, dest):
    Q = deque()
    if source == dest: return True
    Q.append(source)
    while Q:
        curr = Q.popleft()
        if curr == dest:
            return True
        for node in adj[curr]:
            Q.append(node)
    return False


## with depth first traversal

def has_path_depth(adj, source, dest):
    stack = []
    if source == dest: return True
    stack.append(source)

    while stack:
        curr = stack.pop()
        if curr == dest: return True
        for node in adj[curr]:
            stack.append(node)
    return False




if __name__ == "__main__":

    adj_list = {
        'f': ['g', 'i'],
        'g': ['h'],
        'i': ['g', 'k'],
        'j': ['i'],
        'h': [],
        'k': []
    }
    print(has_path(adj=adj_list, source='f', dest='k'))
    print(has_path(adj=adj_list, source='f', dest='j'))

    print("***"*10)
    print(has_path_depth(adj=adj_list, source='f', dest='k'))
    print(has_path_depth(adj=adj_list, source='f', dest='j'))