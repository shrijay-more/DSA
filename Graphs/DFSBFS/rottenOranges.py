# https://leetcode.com/problems/rotting-oranges/
from typing import List
from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        vis = [[0] * cols for _ in range(rows)]
        q = Queue()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    vis[i][j] = 2

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        ans = 0

        while not q.empty():
            row, col, time = q.get()
            ans = max(ans, time)
            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if (0 <= nrow < rows and
                    0 <= ncol < cols and
                    grid[nrow][ncol] == 1 and
                    vis[nrow][ncol] == 0):
                    vis[nrow][ncol] = 2
                    q.put((nrow, ncol, time + 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1

        return ans