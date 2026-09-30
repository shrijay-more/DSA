# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def createLinkedList(self, arr: List[int]):
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
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

LL = LinkedList()
sol = Solution()

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.findMiddle(head)
    LL.display(ans)