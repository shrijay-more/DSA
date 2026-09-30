# https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

from queue import Queue

class Solution:
    def nearest(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]
        dist = [[0] * cols for _ in range(rows)]

        q = Queue()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.put((i, j, 0))
                    vis[i][j] = True

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while not q.empty():
            row, col, step = q.get()
            dist[row][col] = step

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if (0 <= nrow < rows and
                    0 <= ncol < cols and
                    not vis[nrow][ncol]):

                    vis[nrow][ncol] = True
                    q.put((nrow, ncol, step + 1))

        return dist