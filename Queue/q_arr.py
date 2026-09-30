class MyQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return self.rear == self.size - 1

    def enqueue(self, x):
        if self.isFull():
            print("Queue is full")
            return
        
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.queue[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        poppedEle = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return poppedEle

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        return self.queue[self.front]
    
print("Size of queue: ")
size =int(input())
q=  MyQueue(size)
while True:
    print("1. Push 2. Pop x. Exit")
    n = str(input())
    if n == "1":
        print("Enter Element: ")
        ele = int(input())
        q.enqueue(ele)
    
    elif n == "2":
        ele = q.dequeue()
        print(f'dequed element {ele}')
    
    elif n == "x":
        break

    else:
        print("Invalid input")
