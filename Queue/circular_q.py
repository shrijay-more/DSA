class my_queue:
    def __init__(self, capacity):
        self.capactiy = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear  = -1
        
    def enqueue(self,x):
        if (self.rear + 1) % self.capactiy == self.front:
            print("queue is full")
            return

        if self.front == -1:
            self.front,self.rear = 0,0
        
        else:
            self.rear = (self.rear + 1) % self.capactiy

        self.queue[self.rear] = x

    
    def dequeue(self):
        if self.front == -1:
            print("queue is empty")
            return

        poppedEle = self.queue[self.front]

        if self.front == self.rear:
            self.front, self.rear = -1,-1

        else:
            self.front = (self.front+1)%self.capacity
            
        return poppedEle
        

            

        
        
    


    