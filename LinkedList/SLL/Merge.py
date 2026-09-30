from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self, arr):
        self.head = ListNode(arr[0])

        temp = self.head

        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            temp.next = newNode
            temp = newNode

        return self.head

    def display(self, head):

        if head is None:
            print("Linked list is empty")
            return

        temp = head

        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next

        print("None")

class Solution:
    def merge(self, head1, head2):
        dummyNode = ListNode(-1)
        curr = dummyNode
        temp1, temp2 = head1, head2
        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next

            curr = curr.next

        if temp1 is not None:
            curr.next = temp1

        if temp2 is not None:
            curr.next = temp2

        return dummyNode.next

LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    head1 = LL.createLinkedList(nums1)
    head2 = LL.createLinkedList(nums2)
    ans = sol.merge(head1,head2)
    LL.display(ans)