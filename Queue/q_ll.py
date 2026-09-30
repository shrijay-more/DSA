class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next =next

class my_queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
            return
        
        self.rear.next = newNode
        self.rear = newNode


    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return

        poppedEle = self.front.data
        
        if self.front.next:
            self.front = self.front.next
        else:
            self.front = None
            self.rear = None

        return poppedEle


q = my_queue()

while True:
    print("1. enqueue 2. dequeue x. Exit")
    user_input = str(input())
    if user_input == "1":
        print("Enter element: ")
        ele = int(input())
        q.enqueue(ele)
    
    elif user_input == "2":
        ele  = q.dequeue()
        print(f"Popped element: {ele}")
    

    elif user_input == "x":
        break

    else:
        print("Invalid input")

