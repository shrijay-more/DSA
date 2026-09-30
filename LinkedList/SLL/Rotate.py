# https://leetcode.com/problems/rotate-list/

from typing import List,Optional
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
            print("Linked list is empty!")
            return

        temp = head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print("None")

class Solution:
    def rotateRightHelper(self, head:Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next.next is not None:
            temp = temp.next

        newHead = temp.next
        temp.next = None
        newHead.next = head
        return newHead

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        len = 0
        temp =  head
        while temp is not None:
            len+=1
            temp = temp.next
        
        k = k % len
        for i in range(k):
            head = self.rotateRightHelper(head)

        return head
    
LL = LinkedList()
sol = Solution()

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    k = int(input())
    ans = sol.rotateRight(head,k)
    LL.display(ans)