class minStack:
    def __init__(self):
        self.st = []

    def push(self,val):
        if len(self.st)==0:
            self.st.append([val,val])
        else:
            self.st.append([val, min(val, self.st[-1][1])])

    def getMin(self):
        if len(self.st) == 0:
            print("stack is empty")
            return
        
        return self.st[-1][1]

    def top(self):
        if len(self.st) == 0:
            print("stack is empty")
            return
        
        return self.st[-1][0]
    
    def pop(self):
        if len(self.st) == 0:
            print("stack is empty")
            return

        return self.st.pop()
    
    def display(self):
        print(self.st)


class minStackOp:

    def __init__(self):
        self.minimum = float('-inf')
        self.st  = []

    def push(self, val):
        if len(self.st) == 0:
            self.minimum = val
            self.st.append(val)
        else:
            if val > self.minimum:
                self.st.append(val)
            else:
                self.st.append(2*val -  self.minimum)

    def getMin(self):
        if len(self.st) == 0:
            print("Stack is empty!")
            return
        
        return self.minimum
    
    def pop(self):
        if len(self.st) == 0:
            print("Stack is empty!")
            return
        
        x = self.st.pop()

        if x < self.minimum:
            return 2*self.minimum - x
        else:
            return x
        
    def top(self):
        if len(self.st) == 0:
            print("Stack is empty!")
            return
         
        x = self.st[-1]
        if x < self.minimum:
            return 2*self.minimum - x
        else:
            return x
         

ms = minStack()

while True:
    print("1. Push  2. Pop  3.Top   4.GetMin    5.Display   x.Exit")
    user_input = str(input())
    if user_input == "1":
        val = int(input("Enter the val: "))
        ms.push(val)
    elif user_input == "2":
        ms.pop()
    elif user_input == "3":
        print(ms.top())
    elif user_input == "4":
        print(ms.getMin())
    elif user_input =="5":
        ms.display()
    elif user_input == "x":
        break
    else:
        print("invalid input")

