from collections import deque

def breadth_first_traversal(adj, source):
    q = deque()
    q.append(source)
    while q:
        curr = q.popleft()
        print(curr)
        for i in adj[curr]:
            q.append(i)



if __name__ == '__main__':

    adj = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    breadth_first_traversal(adj, 'a')