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
    def merge2Lists(self, head1, head2):
        dummyNode = ListNode(-1)
        curr = dummyNode

        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next

        if head1:
            curr.next = head1

        if head2:
            curr.next = head2

        return dummyNode.next
    
    def findMiddle(self,head):
        slow, fast = head, head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortLL(self, head):
        if head is None or head.next is None:
            return head

        Middle = self.findMiddle(head)
        right = Middle.next
        Middle.next = None
        left = head

        left = self.sortLL(left)
        right = self.sortLL(right)
        return self.merge2Lists(left,right)

LL = LinkedList()
sol = Solution()
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.sortLL(head)
    LL.display(ans)