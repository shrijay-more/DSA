# https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

import heapq

class Solution:
    def shortestPath(self, V, edges, src, dest):

        adj = [[] for _ in range(V + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [float('inf')] * (V + 1)

        parent = [0] * (V + 1)

        for i in range(V + 1):
            parent[i] = i

        heap = []

        dist[src] = 0
        parent[src] = src

        heapq.heappush(heap, (0, src))

        while heap:

            distance, node = heapq.heappop(heap)
            
            if distance > dist[node]:
                continue
            
            for neighbor, wt in adj[node]:

                new_distance = distance + wt

                if new_distance < dist[neighbor]:

                    dist[neighbor] = new_distance

                    parent[neighbor] = node

                    heapq.heappush(
                        heap,
                        (new_distance, neighbor)
                    )
                    
        if dist[dest] == float('inf'):
            return [-1]

        path = []

        node = dest

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(src)

        path.reverse()

        return path

    def shortestPathLex(self, V, edges, src, dest):

        adj = [[] for _ in range(V + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [float('inf')] * (V + 1)

        dist[dest] = 0

        heap = []
        heapq.heappush(heap, (0, dest))

        while heap:

            distance, node = heapq.heappop(heap)

            if distance > dist[node]:
                continue

            for neighbor, wt in adj[node]:

                new_distance = distance + wt

                if new_distance < dist[neighbor]:

                    dist[neighbor] = new_distance

                    heapq.heappush(
                        heap,
                        (new_distance, neighbor)
                    )

        if dist[src] == float('inf'):
            return [-1]

        # Construct lexicographically smallest path
        path = [src]

        node = src

        while node != dest:

            next_node = -1

            for neighbor, wt in adj[node]:

                # This edge belongs to a shortest path
                if dist[node] == dist[neighbor] + wt:

                    # Choose smallest possible next vertex
                    if next_node == -1 or neighbor < next_node:
                        next_node = neighbor

            node = next_node
            path.append(node)

        return path