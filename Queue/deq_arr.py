class my_queue:
    def __init__(self,capacity):
        self.size = 0
        self.queue = [0] * capacity
        self.capacity = capacity
        self.front = 0
    
    def insertFront(self,x):
        if self.size == self.capacity:
            print("dqueue is full")
            return
        
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.queue[self.front] = x
            self.size+=1

    def deleteFront(self):
        if self.size == 0:
            print("dqueue is empty")
            return
        
        else:
            poppedEle = self.queue[self.front]
            self.front = (self.front+1)%self.capacity
            self.size-=1
            return poppedEle
        
    def insertRear(self,x):
        if self.size == self.capacity:
            print("dqueue is full")
            return
        
        new_rear = (self.front + self.size) % self.capacity
        self.queue[new_rear] = x
        self.size+=1

    def deleteRear(self,x):
        if self.size == 0:
            print("dequeue is empty!")
            return
        
        rear = (self.front + self.size - 1) % self.capacity
        poppedEle = self.queue[rear]
        self.size-=1
        return poppedEle
    
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=" ")

        print()

print("Enter dequeue capacity")
n = int(input())
dq = my_queue(n)  
while True:
    print("1. Insert Front 2. Inert Rear 3. Delete Front 4. Delete Rear 5. Display x. Exit")
    usr_input = str(input())
    if usr_input == "1":
        ele = input()
        dq.insertFront(ele)
    elif usr_input == "2":
        ele = input()
        dq.insertRear(ele)
    elif usr_input == "3":
        ele = dq.deleteFront()
        print(f"deleted element is {ele}")
    elif usr_input == "4":
        ele = dq.deleteRear()
        print(f"deleted element is {ele}")
    elif usr_input == "5":
        dq.display()
    elif usr_input == "x":
        break
    else:
        print("Invalid input")






    
    

        
    