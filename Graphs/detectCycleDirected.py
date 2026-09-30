def dfs(node, adj, vis, pathVis):
    
    vis[node] = 1
    pathVis[node] = 1

    for neighbor in adj[node]:
        if not vis[neighbor]:
            if dfs(neighbor, adj, vis, pathVis):
                return True
        elif pathVis[neighbor]:
            return True

    pathVis[node] = 0
    return False


def isCyclic(adjList):
    vis = [0] * len(adjList)
    pathVis = [0] * len(adjList)

    for i in range(len(adjList)):
        if not vis[i]:
            if dfs(i, adjList, vis, pathVis):
                return True

    return False


from queue import Queue

def kahnsAlgoForCycle(V,adj):
    q = Queue()
    indegree = [0] * V

    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor]+=1

    for i in range(V):
        if indegree[i] == 0:
            q.put(i)

    topo = []
    while not q.empty():
        node = q.get()
        topo.append(node)
        for neighbor in adj[node]:
            indegree[neighbor]-=1
            if indegree[neighbor] == 0:
                q.put(neighbor)
                
    return len(topo) == V


n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

print(isCyclic(adj))