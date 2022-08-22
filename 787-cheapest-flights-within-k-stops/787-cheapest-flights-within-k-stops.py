class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """ O(k*E)T O(V)S bellman-ford algo """
        cost = collections.defaultdict(lambda: math.inf)
        cost[src] = 0
        for _ in range(k + 1):
            cost_ = cost.copy()
            for a, b, c in flights:
                if cost_[b] > cost[a] + c:
                    cost_[b] = cost[a] + c
            cost = cost_

        return cost[dst] if cost[dst] != math.inf else -1