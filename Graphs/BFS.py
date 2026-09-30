from queue import Queue

def BFS(adjList, startNode):
    q = Queue()
    vis = [False] * len(adjList)
    ans = []
    vis[startNode] = True
    q.put(startNode)

    while not q.empty():
        node = q.get()
        ans.append(node)

        for neighbor in adjList[node]:
            if not vis[neighbor]:
                vis[neighbor] = True
                q.put(neighbor)

    return ans


n, m = map(int, input().split())

adjList = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    #adjList[v].append(u)   

print(BFS(adjList, 1))