# http://leetcode.com/problems/palindrome-linked-list/description/
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
    def isPalindromeBrute(self, head: Optional[ListNode]) -> bool:
        st = []
        curr = head
        while curr is not None:
            st.append(curr.val)
            curr = curr.next

        curr = head
        while curr is not None:
            if curr.val is not st.pop():
                return False

            curr = curr.next

        return True
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        head1 = head
        head2 = self.reverse(slow.next)

        second_half = head2

        while head2 is not None:
            if head1.val != head2.val:
                self.reverse(second_half)
                return False

            head1 = head1.next
            head2 = head2.next

        self.reverse(second_half)
        return True

LL = LinkedList()
sol = Solution()
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    print(sol.isPalindromeBrute(head))