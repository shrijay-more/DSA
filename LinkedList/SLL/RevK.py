# https://leetcode.com/problems/reverse-nodes-in-k-group/
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
            print("Linked list is empty!")
            return

        temp = head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print("None")
    

class Solution:
    def reverseLL(self, head: Optional[ListNode])->Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        prev = None
        while temp is not None:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode
        return prev

    def findKthNode(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        temp =  head
        cnt = 0 
        while temp is not None:
            cnt+=1
            if cnt == k :
                return temp
            temp = temp.next
        return None

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        prevNode = None
        while temp is not None:
            cnt = k
            kthNode = self.findKthNode(temp,k)
            if kthNode is None:
                if prevNode:
                    prevNode.next = temp
                    break
            nextNode = kthNode.next
            kthNode.next = None
            self.reverseLL(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode

        return head


        
LL = LinkedList()
sol = Solution()
 
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    k = int(input())
    ans = sol.reverseKGroup(head,k)
    LL.display(ans)
