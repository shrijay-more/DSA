class Heap:
    def __init__(self):
        self.arr = [0]*100
        self.size = 0

    def insert(self,val):
        self.size = self.size+1
        index = self.size
        self.arr[index] = val

        while index > 1:
            parent = index//2
            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                break

    def delete(self):
        if self.size == 0:
            print("Nothing to delete")
            return -1

        self.arr[1],self.arr[self.size] = self.arr[self.size],self.arr[1]
        ele = self.arr[self.size]
        self.size-=1

        i = 1
        while i < self.size:
            left = 2 * i
            right = 2*i+1

            if left < self.size and self.arr[i] < self.arr[left]:
                self.arr[i],self.arr[left] = self.arr[left],self.arr[i]
                i = left

            elif right < self.size and self.arr[i] < self.arr[right]:
                self.arr[i],self.arr[right] = self.arr[right],self.arr[i]
                i = right

            else:
                break

        return ele

    def display(self):
        for i in range(1,self.size+1):
            print(self.arr[i],end=" ")

        print()

h = Heap()
h.insert(60)
h.insert(20)
h.insert(70)
h.insert(30)
h.insert(90)

h.display()