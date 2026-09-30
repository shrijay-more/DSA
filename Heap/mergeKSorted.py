# https://www.naukri.com/code360/problems/merge-k-sorted-arrays_975379?leftPanelTab=0&leftPanelTabValue=SUBMISSION
from heapq import heappush, heappop

def mergeKSortedArrays(kArrays, k):
    heap = []
    result = []
    
    for i in range(k):
        if len(kArrays[i]) > 0:
            heappush(heap, (kArrays[i][0], i, 0))

    while heap:
        value, i, j = heappop(heap)
        result.append(value)

        if j + 1 < len(kArrays[i]):
            heappush(heap, (kArrays[i][j + 1], i, j + 1))

    return result

t = int(input())

for _ in range(t):
    mat = []
    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split(" ")))
        mat.append(arr)
    print(mergeKSortedArrays(mat),n)