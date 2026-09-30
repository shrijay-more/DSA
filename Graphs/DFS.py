
def DFSHelper(adjList, startnode,vis,ans):
    vis[startnode] = True
    ans.append(startnode)
    
    for neighbor in adjList[startnode]:
        if not vis[neighbor]:
            DFSHelper(adjList,neighbor,vis,ans)


def DFS(adjList):
    vis=[False] * len(adjList)
    ans = []
    for node in range(1,len(adjList)):
        if not vis[node]:
            DFSHelper(adjList,node,vis,ans)
    return ans

n, m = map(int, input().split())

adjList = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u) 

print(DFS(adjList,1))