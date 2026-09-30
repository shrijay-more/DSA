# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

from queue import Queue

class Solution:
    def shortestPath(self, V, edges, src,dest):

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [10**9] * V
        dist[src] = 0

        q = Queue()
        q.put(src)


        while not q.empty():
            node = q.get()
            
            for neighbor in adj[node]:

                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    q.put(neighbor)


        if dist[dest] == 10**9:
            return -1

        return dist[dest]