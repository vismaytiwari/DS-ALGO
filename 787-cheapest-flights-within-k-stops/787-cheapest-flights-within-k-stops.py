class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for i, j, l in flights:
            graph[i].append([j, l])
            
        minCost = [float('inf')] * n
        q = deque([(src, 0)])
      
    
        stop = -1
        
        while q and stop < k:
            stop += 1
            level = len(q)
            for _ in range(level):
                node, cost = q.popleft()
                for nxtNode, nxtCost in graph[node]:
                    if nxtCost + cost < minCost[nxtNode]:
                        minCost[nxtNode] = cost + nxtCost
                        q.append((nxtNode, nxtCost + cost))
    
        return -1 if minCost[dst] == float('inf') else minCost[dst]
     