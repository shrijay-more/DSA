class my_stack:
    def __init__(self,n):
        self.n = n
        self.arr = [0] * n
        self.index = -1

    def isEmpty(self):
        return (self.index == -1)
    
    def isFull(self):
        return (self.index == self.n - 1)
    
    def push(self,x):
        if self.isFull():
            print("stack is full")
            return
        self.index+=1
        self.arr[self.index] = x

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return

        poppedEle = self.arr[self.index]
        self.index-=1
        return poppedEle
    
print("Size of stack: ")
size =int(input())
st = my_stack(size)
while True:
    print("1. Push 2. Pop x. Exit")
    n = str(input())
    if n == "1":
        print("Enter Element: ")
        ele = int(input())
        st.push(ele)
    
    elif n == "2":
        ele = st.pop()
        print(f'Popped element {ele}')
    
    elif n == "x":
        break

    else:
        print("Invalid input")

    