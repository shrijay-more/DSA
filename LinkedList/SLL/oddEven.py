# https://leetcode.com/problems/odd-even-linked-list/
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead

        return head
    
sol = Solution()
LL = LinkedList()
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.oddEvenList(head)
    LL.display(ans)
