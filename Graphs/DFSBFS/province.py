# https://leetcode.com/problems/number-of-provinces/

from typing import List

class Solution:
    def DFS(self, isConnected, node, vis):
        vis[node] = True

        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1 and not vis[neighbor]:
                self.DFS(isConnected, neighbor, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        cnt = 0
        for node in range(n):
            if not vis[node]:
                cnt += 1
                self.DFS(isConnected, node, vis)

        return cnt


sol = Solution()

n, m = map(int, input().split())

isConnected = [[0] * n for _ in range(n)]

for i in range(n):
    isConnected[i][i] = 1

for _ in range(m):
    u, v = map(int, input().split())
    isConnected[u][v] = 1
    isConnected[v][u] = 1

print(sol.findCircleNum(isConnected))