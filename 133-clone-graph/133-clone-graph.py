"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        m, visited, q = {},set(),[node]
        while q:
            n = q.pop(0)
            if n in visited: continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for ne in n.neighbors:
                if ne not in m:
                    m[ne] = Node(ne.val)
                m[n].neighbors.append(m[ne])
                q.append(ne)
        return m[node]
                
        