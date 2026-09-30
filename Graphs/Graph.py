class Graph:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.adjMat = [[0]* (n+1) for _ in range(n+1)]
        self.adjList = [[] for _ in range(n + 1)]

    def adjMatFunc(self):
        for _ in range(self.m):
            u,v = map(int, input().split(" "))
            self.adjMat[u][v] = 1
            self.adjMat[v][u] = 1

        return self.adjMat

    def adjListFunc(self):
        for _ in range(self.m):
            u,v = map(int, input().split(" "))
            self.adjList[u].append(v)
            self.adjList[v].append(u) 

        return self.adjList

    def adjListFuncWeighted(self):
            for _ in range(self.m):
                u,v,weight = map(int, input().split(" "))
                self.adjList[u].append((v,weight))
                self.adjList[v].append((u,weight)) 
    
            return self.adjList
    
n,m = map(int, input().split(" "))
g = Graph(n,m)

# mat = g.adjMatFunc()
adjList = g.adjListFunc()

for i in range(1, n + 1):
    print(f"{i}: {adjList[i]}")