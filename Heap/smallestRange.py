# https://www.naukri.com/code360/problems/smallest-range-from-k-sorted-list_1069356?leftPanelTab=0

import heapq

def kSorted(a, k, n):
    heap = []
    current_max = float('-inf')

    for i in range(k):
        heapq.heappush(heap, (a[i][0], i, 0))
        current_max = max(current_max, a[i][0])

    best_start = 0
    best_end = float('inf')

    while True:
        current_min, row, col = heapq.heappop(heap)

        if current_max - current_min < best_end - best_start:
            best_start = current_min
            best_end = current_max

        if col + 1 == n:
            break
 
        next_val = a[row][col + 1]

        heapq.heappush(heap, (next_val, row, col + 1))

        current_max = max(current_max, next_val)

    return best_end - best_start + 1

