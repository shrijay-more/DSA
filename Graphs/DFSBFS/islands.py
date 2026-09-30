# https://leetcode.com/problems/number-of-islands/
from typing import List
from queue import Queue

class Solution:
    def BFS(self, ro, co, vis, grid):
        vis[ro][co] = 1
        q = Queue()
        q.put((ro, co))

        n = len(grid)
        m = len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while not q.empty():
            row, col = q.get()

            for dr, dc in directions:
                nrow = row + dr
                ncol = col + dc

                if (
                    0 <= nrow < n
                    and 0 <= ncol < m
                    and grid[nrow][ncol] == "1"
                    and vis[nrow][ncol] == 0
                ):
                    vis[nrow][ncol] = 1
                    q.put((nrow, ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]
        cnt = 0

        for row in range(n):
            for col in range(m):
                if vis[row][col] == 0 and grid[row][col] == "1":
                    cnt += 1
                    self.BFS(row, col, vis, grid)

        return cnt
    def BFS(self, ro,co,vis,grid):
        vis[ro][co] =1 
        q = Queue()
        q.put((ro,co))
        n = len(grid)
        m = len(grid[0])

        while not q.empty():
            row,col = q.get()
            for delrow in range(-1,2):
                for delcol in range(-1,2):
                    nrow = row + delrow
                    ncol = col + delcol
                    if nrow >=0 and nrow < n and ncol >=0 and ncol < m and grid[nrow][ncol] == "1" and vis[nrow][ncol] == 0:
                        vis[nrow][ncol] = 1
                        q.put((nrow,ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]
        cnt = 0
        for row in range(n):
            for col in range(m):
                if vis[row][col] == 0  and grid[row][col] == "1":
                    cnt+=1
                    self.BFS(row,col,vis,grid)

        return cnt