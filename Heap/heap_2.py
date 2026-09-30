def heapify(arr, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def createMaxHeap(arr):
    n = len(arr) - 1
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)


def heapSort(arr, n):
    t = n
    while t > 1:
        arr[1], arr[t] = arr[t], arr[1]
        t -= 1
        heapify(arr, t, 1)


arr = [-1, 54, 53, 55, 52, 50]

createMaxHeap(arr)
print(arr)

heapSort(arr, len(arr) - 1)
print(arr)