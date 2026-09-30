from typing import List

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev =  prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def createLinkedList(self, arr):
        self.head = ListNode(arr[0])
        temp = self.head
        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            newNode.prev = temp
            temp.next = newNode
            temp = newNode

        return self.head
    
    def display(self, head):
        if head is None:
            print("Linked list is empty!")
            return

        temp = head
        while temp is not None:
            print(temp.val, end="<-->")
            temp = temp.next

        print("None")


class Solution:
    def removeDups(self, head):
        if head is None or head.next is None:
            return head
        
        temp = head
        while temp != None and temp.next is not None:
            nextNode = temp.next
            while nextNode is not None and nextNode.val == temp.val:
                nextNode = nextNode.next
            temp.next = nextNode
            if nextNode:
                nextNode.prev = temp
            temp = temp.next

        return head
    

LL = LinkedList()
sol = Solution()
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.removeDups(head)
    LL.display(ans)
