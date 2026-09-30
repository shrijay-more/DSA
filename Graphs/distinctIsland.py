class Solution:
    def DFS(self, grid, vis, row, col, baseRow, baseCol, shape):
        vis[row][col] = True

        shape.append((row - baseRow, col - baseCol))

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]

            if (0 <= nrow < len(grid) and
                0 <= ncol < len(grid[0]) and
                not vis[nrow][ncol] and
                grid[nrow][ncol] == 1):

                self.DFS(grid,vis,nrow,ncol,baseRow,baseCol,shape)

    def countDistinctIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]

        distinct = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not vis[i][j]:
                    shape = []
                    self.DFS(grid,vis,i,j,i,j,shape)
                    distinct.add(tuple(shape))

        return len(distinct)