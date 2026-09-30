# https://leetcode.com/problems/cheapest-flights-within-k-stops/
from queue import Queue

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        dist = [float('inf')] * n

        for u, v, w in flights:
            adj[u].append((v, w))

        q = Queue()
        q.put((0, src, 0))   # stops, node, cost

        dist[src] = 0

        while not q.empty():
            stops, node, cost = q.get()

            if stops > k:
                continue

            for neighbor, price in adj[node]:
                new_cost = cost + price

                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    q.put((stops + 1, neighbor, new_cost))

        if dist[dst] == float('inf'):
            return -1
        else:
            return dist[dst]