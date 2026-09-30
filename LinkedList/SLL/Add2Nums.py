# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional
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
            print("Linked list is empty")
            return

        temp = head

        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next

        print("None")


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummyNode = ListNode(-1)

        temp1 = l1
        temp2 = l2
        curr = dummyNode

        carry = 0

        while temp1 is not None or temp2 is not None:

            total = carry

            if temp1:
                total += temp1.val
                temp1 = temp1.next

            if temp2:
                total += temp2.val
                temp2 = temp2.next

            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummyNode.next


LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    head1 = LL.createLinkedList(arr1)
    head2 = LL.createLinkedList(arr2)

    ans = sol.addTwoNumbers(head1, head2)

    LL.display(ans)