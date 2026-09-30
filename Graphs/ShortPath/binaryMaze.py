# https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1

from queue import Queue

class Solution:
    def shortestPath(self, mat: list[list[int]], src: list[int], dest: list[int]) -> int:
        if mat[src[0]][src[1]] == 0 or mat[dest[0]][dest[1]] == 0:
            return -1
            
        if src == dest:
            return 0
            
        n = len(mat)
        m = len(mat[0])

        q = Queue()
        q.put((0, src[0], src[1]))

        dist = [[float('inf')] * m for _ in range(n)]
        dist[src[0]][src[1]] = 0

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while not q.empty():

            dis, row, col = q.get()

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if (0 <= nrow < n and
                    0 <= ncol < m and
                    mat[nrow][ncol] == 1 and
                    dis + 1 < dist[nrow][ncol]):

                    dist[nrow][ncol] = dis + 1

                    if nrow == dest[0] and ncol == dest[1]:
                        return dis + 1

                    q.put((dis + 1, nrow, ncol))

        return -1