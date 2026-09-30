from queue import Queue
# 1. prerequisite tasks https://www.geeksforgeeks.org/problems/prerequisite-tasks/1 --  can be solved with toposort 
# just check for cycle
# 2. Course Schedular https://leetcode.com/problems/course-schedule/ -- can be solved with toposort 
# just check for cycle

def dfs(node, vis, st,adj):
    vis[node] = True
    for neighbor in adj[node]:
        if not vis[neighbor]:
            dfs(neighbor,vis,st,adj)

    st.append(node)

def toposort(V,adj):
    vis = [False] * V
    st = []
    ans = []
    for i in range(V):
        if not vis[i]:
            dfs(i,vis,st,adj)

    for i in range(len(st)):
        ans.append(st[-1])
        st.pop()

    return ans 



def kahnsAlgo(V,adj):
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
                

    return topo

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

print(toposort(n,adj))