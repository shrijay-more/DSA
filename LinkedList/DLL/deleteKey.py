from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self, arr):
        if not arr:
            return None

        self.head = ListNode(arr[0])
        back = self.head

        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            back.next = newNode
            newNode.prev = back
            back = newNode

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
    def deleteOccurences(self, head, key):
        if head is None:
            return None

        temp = head

        while temp is not None:
            if temp.val == key:
                nextNode = temp.next
                prevNode = temp.prev

                if temp == head:
                    head = nextNode
                    if head is not None:
                        head.prev = None
                else:
                    if prevNode is not None:
                        prevNode.next = nextNode

                    if nextNode is not None:
                        nextNode.prev = prevNode

                temp = nextNode

            else:
                temp = temp.next
        return head
    

    
LL = LinkedList()
sol = Solution()

head = LL.createLinkedList([10, 4, 10, 10, 6, 10, 8])

print("Before deletion:")
LL.display(head)

head = sol.deleteOccurences(head, 10)

print("After deletion:")
LL.display(head)