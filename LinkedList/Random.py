# https://leetcode.com/problems/copy-list-with-random-pointer/description/
from typing import List,Optional
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self,arr):
            self.head = Node(arr[0])
            temp = self.head
            for i in range(1, len(arr)):
                newNode = Node(arr[i])
                temp.next = newNode
                temp = newNode
            
            self.head.random = None
            self.head.next.random = self.head
            self.head.next.next.random = self.head.next

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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp = head

        while temp is not None:
            newNode = Node(temp.val)

            newNode.next = temp.next
            temp.next = newNode

            temp = newNode.next


        temp = head

        while temp is not None:
            copyNode = temp.next

            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None

            temp = copyNode.next


        temp = head

        dummyNode = Node(-1)
        curr = dummyNode

        while temp is not None:
            copyNode = temp.next

            curr.next = copyNode
            curr = copyNode

            temp.next = copyNode.next

            temp = temp.next

        return dummyNode.next
    
    def copyRandomListBrute(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        temp = head
        mpp = dict()
        while temp is not None:
            newNode = Node(temp.val)
            mpp[temp] = newNode
            temp = temp.next
        
        temp = head

        while temp is not None:
            copyNode = mpp[temp]
            copyNode.next = mpp.get(temp.next)
            copyNode.random = mpp.get(temp.random)
            temp = temp.next
        
        return mpp[head]
    
LL = LinkedList()

sol = Solution()

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.copyRandomListBrute(head)
    LL.display(ans)