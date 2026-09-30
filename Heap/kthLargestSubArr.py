import heapq

def getKthLargest(arr, k):
	heap = []

	for i in range(len(arr)):
		sum = 0
		for j in range(i,len(arr)):
			sum+=arr[j]
			
			if len(heap) < k:
				heapq.heappush(heap,sum)
			else:
				if sum > heap[0]:
					heapq.heappop(heap)
					heapq.heappush(heap, sum)

	return heap[0]

t = int(input())

for _ in range(t):
	arr = list(map(int, input().split(" ")))
	print(getKthLargest(arr))