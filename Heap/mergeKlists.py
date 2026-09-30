# https://www.naukri.com/code360/problems/merge-k-sorted-lists_992772?leftPanelTab=0&leftPanelTabValue=SUBMISSION
import heapq
def mergeKLists(listArray):
    heap = []

    for i, head in enumerate(listArray):
        if head:
            heapq.heappush(heap, (head.data, i, head))

    head = None
    tail = None

    while heap:
        _, i, node = heapq.heappop(heap)

        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.data, i, node.next))

    tail.next = None
    return head