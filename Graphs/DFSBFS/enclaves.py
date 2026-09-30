# https://leetcode.com/problems/number-of-enclaves/

from typing import List
class Solution:
    def DFS(self, grid,vis,row,col,delRow,delCol):
        vis[row][col] = True

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]

            if (0 <= nrow < len(grid) and
                0 <= ncol < len(grid[0]) and
                not vis[nrow][ncol] and
                grid[nrow][ncol] == 1):

                self.DFS(grid, vis, nrow, ncol, delRow, delCol)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        for i in range(rows):
            for j in range(cols):
                if ((i == 0 or i == rows -1 or j == 0 or j == cols -1) and grid[i][j] == 1):
                    self.DFS(grid,vis,i,j,delRow,delCol)

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not vis[i][j]:
                    cnt+=1

        return cnt



