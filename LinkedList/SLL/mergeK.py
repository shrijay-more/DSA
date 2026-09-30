from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def createLinkedList(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        temp = head

        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return head

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

    def mergeK(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = lists[0]

        for i in range(1, len(lists)):
            head = self.merge2Lists(head, lists[i])

        return head


LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):
    lists =[]
    n = int(input())
    for i in range(n):
        nums = list(map(int, input().split()))
        head = LL.createLinkedList(nums)
        lists.append(head)

    ans = sol.mergeK(lists)
    LL.display(ans)