class Node:
    def __init__(self, data:int, next:Node):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data:int):
        if self.head == None:
            self.head = Node(data, None)
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = Node(data, None)

    def delete(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
            
        temp.next = None
    
    def insertHead(self, data:int):
        if self.isEmpty():
            self.head = Node(data, None)
            return

        temp  = self.head
        self.head = Node(data, None)
        self.head.next = temp

    def deleteHead(self):
        if self.isEmpty():
            print("Linked list is empty")
            return
        
        self.head = self.head.next

    def insertAtIndex(self, data: int, index: int):
        if index <= 0:
            print("Invalid index")
            return
        if index == 1:
            self.insertHead(data)
            return
        
        temp = self.head
        prev = None
        while temp is not None and index > 1:
            prev = temp
            temp = temp.next
            index -= 1

        if prev is None:
            print("Invalid index")
            return
        newNode = Node(data, temp)
        prev.next = newNode

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def display(self):
        if self.isEmpty():
            print("Linked list is empty")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

        print("None")

    def deleteAtIndex(self, index:int):
        if self.isEmpty():
            print("Linked List in empty")
            return
        if index <= 0:
            print("Invalid index")
            return
        if index == 1:
            self.head = self.head.next
            return
        
        cnt = 1
        curr = self.head
        prev = None
        while curr is not None:
            if cnt == index:
                prev.next = curr.next
                curr.next = None
                return
            prev = curr
            curr = curr.next
            cnt+=1

        print("Index out of range")

    def reverseIterative(self):
        if self.isEmpty():
            print("Linked list is empty")
            return

        temp = self.head
        prev = None
        while temp is not None:
            currTemp = temp
            temp = temp.next
            currTemp.next = prev
            prev = currTemp
            
        self.head  = prev

    def reverseHelper(self, curr, prev):
        if curr == None:
            self.head =  prev
            return
        
        nextNode = curr.next
        curr.next = prev
        prev = curr
        self.reverseHelper(nextNode, prev)

    def reverse(self):
        self.reverseHelper(self.head, None)


l1 = LinkedList()
l1.insert(5)
l1.insert(8)
l1.insert(12)
l1.insert(34)
l1.display()
l1.reverse()
l1.display()