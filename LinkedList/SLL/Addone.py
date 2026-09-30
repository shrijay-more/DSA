# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
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
    def reverse(self, head):
        if head is None or head.next is None:
            return head
            
        curr = head
        prev = None
        
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev
        
    def addOne(self,head):
        carry = 1

        head = self.reverse(head)

        temp = head

        while temp is not None:
            summ = carry + temp.data

            temp.data = summ % 10
            carry = summ // 10

            if carry == 0:
                break
            
            if temp.next is None:
                temp.next = ListNode(carry)
                carry = 0
                break

            temp = temp.next

        head = self.reverse(head)

        return head
    

    def addOneHelper(self,head):
        if head is None:
            return 1
        
        carry = self.addOneHelper(head.next)
        head.data = head.data + carry
        
        if head.data < 10:
            return 0
        
        head.data = 0
        return 1
        
    def addOneOptimal(self,head):
        # code here
        carry = self.addOneHelper(head)
        if carry == 1:
            newNode = ListNode(1)
            newNode.next = head
            head = newNode
            
        return head
        
        
    
LL = LinkedList()
sol = Solution()

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    head = LL.createLinkedList(nums)
    ans = sol.addOne(head)
    LL.display(ans)