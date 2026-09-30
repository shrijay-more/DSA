import heapq

class Solution:
    def kthSmallest(self, arr, k):
        heap = []
        i = 0
        while i < k:
            heapq.heappush(heap, -arr[i])
            i += 1

        while i < len(arr):
            if heap[0] < -arr[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])
            i += 1

        return -heap[0]

sol = Solution()

t = int(input())

for i in range(t):
    arr = list(map(int, input().split(" ")))
    k = int(input())
    print(sol.kthSmallest(arr,k))
