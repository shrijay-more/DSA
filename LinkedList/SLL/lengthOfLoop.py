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
    def findLength(self, slow, fast):
        cnt = 1
        fast = fast.next
        while fast != slow:
            cnt+=1
            fast = fast.next

        return cnt
    
    def getLoopLength(self, head:Optional[ListNode]):
        slow, fast = head,head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return self.findLength(slow,fast)
            
        return 0
    
LL = LinkedList()

head = LL.createLinkedList([1, 2, 3, 4, 5])

temp = head
thirdNode = None

while temp.next is not None:
    if temp.val == 3:
        thirdNode = temp
    temp = temp.next

temp.next = thirdNode

sol = Solution()
print(sol.getLoopLength(head))