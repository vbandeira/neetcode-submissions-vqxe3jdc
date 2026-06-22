"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(curr):
            if curr in graph:
                return graph[curr]
            
            graph[curr] = Node(curr.val)
            for n in curr.neighbors:
                graph[curr].neighbors.append(dfs(n))
            return graph[curr]

        graph = defaultdict(Node)
        return dfs(node) if node else None
