# https://leetcode.com/problems/linked-list-cycle-ii/submissions/2002311564/
from typing import List,Optional

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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head is None or head.next is None:
            return None
            
        mpp = dict()
        temp = head
        while temp is not None:
            if temp in mpp:
                return temp

            mpp[temp] =True
            temp = temp.next

        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        else:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    
LL = LinkedList()
sol  =Solution()

nums = [1,2,3,4,5,6]
head = LL.createLinkedList(nums)
temp = head

while temp.next is not None:
    temp = temp.next

temp.next = head.next.next.next

ans = sol.detectCycle(head)
LL.display(ans)