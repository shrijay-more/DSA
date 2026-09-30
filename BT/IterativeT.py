class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        pass    
        self.idx = 0 

    def createTree(self,arr):
        if self.idx >= len(arr):
            return None
        
        if arr[self.idx] == -1:
            self.idx+=1
            return None
        
        root = TreeNode(arr[self.idx])
        self.idx+=1
        root.left = self.createTree(arr)
        root.right = self.createTree(arr)
        return root
    
    def IterativePreorder(self, root):
        if root is None:
            return
        
        st = [root]

        while st:
            node = st.pop()
            print(node.data, end=" ")

            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

    
    def IterativeInorder(self,root):
        if root is None:
            return
        
        st = []
        curr =  root  

        while curr is not None or st:
            while curr is not None:
                st.append(curr)
                curr = curr.left

            curr = st.pop()
            print(curr.data, end= " ")

            curr = curr.right

    def IterativePostorder(self,root):
        if root is None:
            return

        st1 = [root]
        st2 = []

        while st1:
            node = st1.pop()
            st2.append(node.data)

            if node.left:
                st1.append(node.left)

            if node.right:
                st1.append(node.right)

        while st2:
            print(st2.pop(),end=" ")


    def IterativePostorderOptimal(self,root):
        if root is None:
            return

        curr = root
        st = []

        while curr is not None or st:
            if curr is not None:
                st.append(curr)
                curr = curr.left
            
            else:
                temp = st[-1].right
                if temp is None:
                    temp = st.pop()
                    print(temp.data,end=" ")
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        print(temp.data, end=" ")
                else:
                    curr = temp

# 1 2 4 -1 -1 5 -1 -1 3 -1 6 -1 -1

arr = list(map(int, input().split()))

BT = BinaryTree()
root  = BT.createTree(arr)

print("Inorder: ",end=" ")
BT.IterativeInorder(root)
print()

print("Postorder",end=" ")
BT.IterativePostorder(root)
print()

print("Preorder",end=" ")
BT.IterativePreorder(root)