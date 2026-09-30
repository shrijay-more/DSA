def heapify(arr, index, n):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, n)


def buildHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)


def merge2Heaps(arr1, arr2):
    arr1.extend(arr2)
    buildHeap(arr1)
    return arr1


t = int(input())

for _ in range(t):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(merge2Heaps(arr1, arr2))