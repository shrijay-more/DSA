# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        slow = head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
    
LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.removeNthFromEnd(head)
    LL.display(ans)