class Node:
    def __init__(self,data=0, next=None):
        self.data = data
        self.next = next
        
class my_stack:
    def __init__(self):
        self.head = None

    def push(self,x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            self.next =  None
            return

        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head is None:
            print("Stack is empty!")
            return
        
        poppedEle = self.head.data

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        
        return poppedEle

    def display(self):
        if self.head is None:
            print("Stack is empty!")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    
st = my_stack()

while True:
    print("1. Push 2. Pop 3. Display x. Exit")
    user_input = str(input())
    if user_input == "1":
        print("Enter element: ")
        ele = int(input())
        st.push(ele)
    
    elif user_input == "2":
        ele  = st.pop()
        print(f"Popped element: {ele}")
    
    elif user_input == "3":
        st.display()

    elif user_input == "x":
        break

    else:
        print("Invalid input")

