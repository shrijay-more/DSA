# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from queue import Queue
class BFS:
    def isCycle(self, V, edges):
                adj = [[] for _ in range(V)]
                for u,v in edges:
                    adj[u].append(v)
                    adj[v].append(u)
                
                vis = [False] * V 
                
                for i in range(V):
                    if not vis[i]:
                        if self.detect(i,adj,vis):
                            return True
                
                return False
    
    def detect(self, src, adj,vis):
        q = Queue()
        q.put((src,-1))
        vis[src] = True
        
        while not q.empty():
            node, parent = q.get()
            
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    vis[neighbor] = True
                    q.put((neighbor, node))
                    
                elif neighbor != parent:
                    return True
                    
        return False

class DFS_:
    def isCycle(self, V, edges):
            adj = [[] for _ in range(V)]
            for u,v in edges:
                adj[u].append(v)
                adj[v].append(u)
                
            vis = [False] * V
            
            for i in range(V):
                if not vis[i]:
                    if self.DFS(i,-1,vis,adj):
                        return True
                        
            return False
    
    def DFS(self,node,parent,vis,adj):
        vis[node] = True
        
        for neighbor in adj[node]:
            if not vis[neighbor]:
                if self.DFS(neighbor,node,vis,adj):
                    return True
                    
            elif parent != neighbor:
                return True
                    
        return False
                    
                    
	