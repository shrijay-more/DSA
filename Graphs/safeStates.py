# https://www.geeksforgeeks.org/problems/eventual-safe-states/1

class Solution:
    def dfs(self, node, adj, vis, pathVis, check):
        vis[node] = 1
        pathVis[node] = 1
        check[node] = 0
        for neighbor in adj[node]:
            if not vis[neighbor]:
                if self.dfs(neighbor, adj, vis, pathVis, check):
                    return True
            elif pathVis[neighbor]:
                return True

        pathVis[node] = 0
        check[node] = 1
        return False

    def safeNodes(self, V, edges):
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        vis = [0] * V
        pathVis = [0] * V
        check = [0] * V

        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, pathVis, check)

        ans = []
        for i in range(V):
            if check[i] == 1:
                ans.append(i)

        return ans


from queue import Queue

class SolutionTopo:
    def safeNodes(self, V, edges):
        
        for arr in edges:
            arr.reverse()
            
        adj = [[] for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            
        indegree = [0] * V
        
        q = Queue()
        
        topo  = []
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
                
        for i in range(V):
            if indegree[i] == 0:
                q.put(i)
                
        while not q.empty():
            node = q.get()
            topo.append(node)
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.put(neighbor)
                    
        topo.sort()
        
        return topo
            
            
            
