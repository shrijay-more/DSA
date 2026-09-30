# https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1

class Solution:
    def DFS(self, grid, vis, row, col, delRow, delCol):
        vis[row][col] = True

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]

            if (0 <= nrow < len(grid) and
                0 <= ncol < len(grid[0]) and
                not vis[nrow][ncol] and
                grid[nrow][ncol] == 'O'):

                self.DFS(grid, vis, nrow, ncol, delRow, delCol)

    def fill(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        for i in range(rows):
            for j in range(cols):
                if ((i == 0 or i == rows - 1 or j == 0 or j == cols - 1)
                        and grid[i][j] == 'O'
                        and not vis[i][j]):

                    self.DFS(grid, vis, i, j, delRow, delCol)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O' and not vis[i][j]:
                    grid[i][j] = 'X'

        return grid
    def DFS(self, grid, vis, row, col, delRow, delCol):
        vis[row][col] = True

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]

            if (0 <= nrow < len(grid) and
                0 <= ncol < len(grid[0]) and
                not vis[nrow][ncol] and
                grid[nrow][ncol] == '0'):

                self.DFS(grid, vis, nrow, ncol, delRow, delCol)

    def fill(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        for i in range(rows):
            for j in range(cols):
                if ((i == 0 or i == rows - 1 or j == 0 or j == cols - 1)
                        and grid[i][j] == '0'
                        and not vis[i][j]):

                    self.DFS(grid, vis, i, j, delRow, delCol)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0' and not vis[i][j]:
                    grid[i][j] = 'X'

        return grid