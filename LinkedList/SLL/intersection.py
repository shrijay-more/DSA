# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
from typing import List, Optional

class ListNode:
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
            temp = temp.next
        
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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1



common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)


headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common


headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common


ll = LinkedList()

print("List A:")
ll.display(headA)

print("List B:")
ll.display(headB)


sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)

if intersection:
    print("Intersection Node Value:", intersection.val)
else:
    print("No Intersection")