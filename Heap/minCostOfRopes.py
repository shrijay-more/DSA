import heapq
class Solution:
    def minCost(self, arr):
        heap = []
        
        for num in arr:
            heapq.heappush(heap,num)

        ans = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            s = a + b
            ans += s

            heapq.heappush(heap, s)

        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split(" ")))
    print(sol.minCost(arr))