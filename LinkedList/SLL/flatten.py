from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


class LinkedList:
    def __init__(self):
        self.head = None

    def createLL(self, arr:List[int]) -> Optional[ListNode]:
        self.head = ListNode(arr[0])
        temp = self.head
        for i in range(1,len(arr)):
            newNode = ListNode(arr[i])
            temp.child = newNode
            temp = newNode

        return self.head
    
    def createLinkedList(self, arrays: List[List[int]]) -> Optional[ListNode]:
        if not arrays or not arrays[0]:
            return None

        main_arr = arrays[0]

        self.head = ListNode(main_arr[0])
        temp = self.head

        for i in range(1, len(main_arr)):
            newNode = ListNode(main_arr[i])
            temp.next = newNode
            temp = newNode

        temp = self.head

        for i in range(1, len(arrays)):
            if temp is None:
                break
            nums = arrays[i]
            curr_temp = temp
            for j in range(len(nums)):
                newNode = ListNode(nums[j])
                curr_temp.child = newNode
                curr_temp = curr_temp.child
            temp = temp.next
        return self.head

    def display(self, head: Optional[ListNode]):
        temp = head

        while temp is not None:
            print(temp.val, end="->")
            temp = temp.child
        
        print()


class Solution:
    def flattenBrute(self, head):
        if head is None:
            return None
        arr = []
        temp = head

        while temp is not None:
            arr.append(temp.val)
            if temp.child:
                t2 = temp.child
                while t2 is not None:
                    arr.append(t2.val)
                    t2 = t2.child
            temp = temp.next
        
        arr.sort()
        self.head = LL.createLL(arr)
        LL.display(self.head)

    def mergeTwoLists(self, head1, head2):
        dummyNode = ListNode(-1)
        res = dummyNode

        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                res.child = head1
                res = head1
                head1 = head1.child
            else:
                res.child = head2
                res = head2
                head2 = head2.child

            res.next = None

        if head1:
            res.child = head1

        if head2:
            res.child = head2

        return dummyNode.child

    def flatten(self, head):
        if head is None or head.next is None:
            return head
        mergedHead = self.flatten(head.next)
        head.next = None
        return self.mergeTwoLists(head, mergedHead)
        
LL = LinkedList()
sol = Solution()
t = int(input())

for _ in range(t):
    arrays = []
    n = int(input())
    main_nums = list(map(int, input().split()))
    arrays.append(main_nums)
    for i in range(n):
        nums = list(map(int, input().split()))
        arrays.append(nums)
    head = LL.createLinkedList(arrays)
    sol.flattenBrute(head)
