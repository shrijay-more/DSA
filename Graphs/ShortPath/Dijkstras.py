# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

import heapq
class Solution:
    def dijkstra_PQ(self, V: int, edges: list[list[int]], src: int) -> list[int]:

        adj = [[] for _ in range(V)]
        
        for arr in edges:
            adj[arr[0]].append((arr[1],arr[2]))
            adj[arr[1]].append((arr[0],arr[2]))
            
        heap = []
        
        heapq.heappush(heap,(0,src))
        
        dist = [10**9+7] * V
        dist[src] = 0
        
        while heap:
            
            d,node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            
            for neighbor,wt in adj[node]:
                new_dist = d + wt
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap,(new_dist, neighbor))
                    
        
        return dist

    def dijkstra_Set(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        adj = [[] for _ in range(V)]
        for arr in edges:
            adj[arr[0]].append((arr[1],arr[2]))
            adj[arr[1]].append((arr[0],arr[2]))
            
        st = set()
        st.add((0,src))
        dist = [float('inf')] * V
        dist[src] = 0
        
        
        while st:
            distance,node = min(st)
            st.discard((distance,node))
            
            if distance != dist[node]:
                continue
            
            for neighbor, wt in adj[node]:
                if distance + wt < dist[neighbor]:
                    st.discard((dist[neighbor],neighbor))
                    
                    dist[neighbor] = distance+wt
                    
                    st.add((distance+wt,neighbor))
            
            
        return dist
        