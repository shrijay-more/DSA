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
    def findPairs(self, head, x):
        ans = []

        if head is None:
            return ans

        temp = head
        tail = head

        while tail.next is not None:
            tail = tail.next

        while temp != tail and tail.next != temp:
            total = temp.val + tail.val
            if total > x:
                tail = tail.prev
            elif total < x:
                temp = temp.next
            else:
                ans.append((temp.val, tail.val))
                temp = temp.next
                tail = tail.prev
        return ans

LL = LinkedList()
sol = Solution()
t = int(input())
for _ in range(t):
    nums = list(map(int , input().split()))
    head = LL.createLinkedList(nums)
    x = int(input())
    ans = sol.findPairs(head,x)
    print(ans)


