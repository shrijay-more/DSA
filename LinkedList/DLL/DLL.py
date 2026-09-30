class Node:
    def __init__(self, data:int, next:None, prev:None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data:int):
        newNode = Node(data,None,None)
        if self.head is None:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = newNode
        newNode.prev = curr

    def delete(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        
        curr  = self.head
        while curr.next is not None:
            curr = curr.next

        curr.prev.next = None
        curr.prev = None

    def insertHead(self, data:int):
        newNode = Node(data,None,None)
        if self.head is None:
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def deleteHead(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        
        newHead = self.head.next
        newHead.prev = None
        self.head.next = None
        self.head = newHead

    def insertAtIndex(self, data:int, index:int):
        if index <=0:
            print("Invalid index")
            return
        
        if index == 1:
            self.insertHead(data)
            return
        
        curr = self.head
        cnt = 1

        while curr is not None:
            if cnt == index:
                newNode = Node(data)
                curr.prev.next = newNode
                newNode.next = curr
                newNode.prev = curr.prev
                curr.prev = newNode
                return
            
            cnt+=1
            curr = curr.next

        if cnt == index:
            self.insert(data)
            return
        
        print("Invalid index")


    def deleteAtIndex(self,index:int):
        if index <=0:
            print("Invalid index")
            return

        if self.head is None:
            print("Linked list is empty")
            return
        
        if index == 1:
            self.deleteHead()
            return
        
        cnt = 1
        curr = self.head

        while curr is not None:
            if cnt == index:
                curr.prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                curr.next = None
                curr.prev = None
                return
            cnt+=1
            curr = curr.next
        
        print("Invalid index")

        
    def reverse(self):

        if self.head is None:
            print("Linked list is empty")
            return

        curr = self.head
        prevNode = None

        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            prevNode = curr
            curr = curr.prev

        self.head = prevNode


    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        curr = self.head
        while curr is not None:
            print(curr.data, end="<->")
            curr = curr.next
        
        print("None")

    
dl1 = DoublyLinkedList()
dl1.insert(12)
dl1.insert(13)
dl1.insert(14)
dl1.insert(15)
dl1.display()
dl1.delete()
dl1.display()
dl1.insertHead(56)
dl1.display()
dl1.deleteHead()
dl1.display()