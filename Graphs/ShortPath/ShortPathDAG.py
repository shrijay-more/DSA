# https://www.geeksforgeeks.org/problems/shortest-path-in-directed-acyclic-graph/1

from queue import Queue

class Solution:
    def TopoSort(self, V: int, adj: list[list[int]]) -> list[int]:
        indegree = [0] * V

        for i in range(V):
            for neighbor, weight in adj[i]:
                indegree[neighbor] += 1

        q = Queue()

        for i in range(V):
            if indegree[i] == 0:
                q.put(i)

        topo = []

        while not q.empty():
            node = q.get()
            topo.append(node)

            for neighbor, weight in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.put(neighbor)

        return topo

    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]

        for arr in edges:
            adj[arr[0]].append((arr[1], arr[2]))

        topo = self.TopoSort(V, adj)

        dist = [10**9] * V
        dist[0] = 0

        for node in topo:
            if dist[node] != 10**9:
                for neighbor, weight in adj[node]:

                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight

        for i in range(V):
            if dist[i] == 10**9:
                dist[i] = -1

        return dist