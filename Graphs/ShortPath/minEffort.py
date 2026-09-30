# https://leetcode.com/problems/path-with-minimum-effort/
from typing import List

import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        n = len(heights)
        m = len(heights[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            diff, row, col = heapq.heappop(heap)

            if diff > dist[row][col]:
                continue

            if row == n - 1 and col == m - 1:
                return diff

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if 0 <= nrow < n and 0 <= ncol < m:

                    newEffort = max(
                        diff,
                        abs(heights[row][col] - heights[nrow][ncol])
                    )

                    if newEffort < dist[nrow][ncol]:
                        dist[nrow][ncol] = newEffort
                        heapq.heappush(
                            heap,
                            (newEffort, nrow, ncol)
                        )

        return dist[n - 1][m - 1]