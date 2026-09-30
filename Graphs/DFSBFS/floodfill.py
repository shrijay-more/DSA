# https://leetcode.com/problems/flood-fill/
from typing import List

class Solution:
    def DFS(self, row, col, ans, image, newColor, delRow, delCol, iniColor):
        ans[row][col] = newColor
        n = len(image)
        m = len(image[0])

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]

            if (0 <= nrow < n and
                0 <= ncol < m and
                image[nrow][ncol] == iniColor and
                ans[nrow][ncol] != newColor):

                self.DFS(nrow, ncol, ans, image, newColor,
                         delRow, delCol, iniColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  color: int) -> List[List[int]]:

        iniColor = image[sr][sc]

        if iniColor == color:
            return image

        rows = len(image)
        cols = len(image[0])

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        ans = [row[:] for row in image]

        self.DFS(sr, sc, ans, image, color, delRow, delCol, iniColor)

        return ans


sol = Solution()

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    image = []

    for _ in range(n):
        arr = list(map(int, input().split()))
        image.append(arr)

    sr, sc, color = map(int, input().split())

    ans = sol.floodFill(image, sr, sc, color)

    for row in ans:
        print(*row)