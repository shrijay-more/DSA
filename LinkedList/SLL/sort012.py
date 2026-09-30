# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
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
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

class Solution:
    def segregate(self, head):
        zeros = ListNode(-1)
        ones = ListNode(-1)
        twos = ListNode(-1)
        zerosHead = zeros
        onesHead = ones
        twosHead = twos
        
        curr = head
        while curr is not None:
            if curr.data == 0:
                zeros.next = curr
                zeros = zeros.next
            elif curr.data == 1:
                ones.next = curr
                ones = ones.next
            else:
                twos.next = curr
                twos = twos.next
            
            curr = curr.next
        
        zeros.next = onesHead.next if onesHead.next else twosHead.next
        ones.next = twosHead.next
        twos.next = None
        
        if zerosHead.next:
            return zerosHead.next
        elif onesHead.next:
            return onesHead.next
        else:
            return twosHead.next
        

t = int(input())
LL = LinkedList()
sol = Solution()
for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.segregate(head)
    LL.display(ans)