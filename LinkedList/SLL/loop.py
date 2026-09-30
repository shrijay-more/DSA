# https://leetcode.com/problems/linked-list-cycle/
from typing import List, Optional

class ListNode :
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def createLinkedList(self, arr:List[int]):
        self.head = ListNode(arr[0])
        temp = self.head
        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            temp.next = newNode
            temp = newNode

        return self.head
    
    def display(self, head):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
       
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    

LL = LinkedList()
sol = Solution()

arr = [1,2,3,4,5]
head = LL.createLinkedList(arr)
temp = head 

while temp.next is not None:
    temp = temp.next

temp.next = head.next.next

print(sol.hasCycle(head))

