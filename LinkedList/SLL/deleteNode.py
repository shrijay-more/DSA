# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional

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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
    

LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.deleteMiddle(head)
    LL.display(ans)