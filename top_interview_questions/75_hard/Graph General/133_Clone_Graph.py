"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}

        def dfs(node):
            if node not in visited:
                copied_node = Node(node.val)
                visited[node] = copied_node
                for neigh in node.neighbors:
                    copied_node.neighbors.append(dfs(neigh))
            return visited[node]
        return dfs(node)
