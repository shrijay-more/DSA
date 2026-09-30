from queue import Queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        pass

    def createTree(self):
        data = int(input())
        if data == -1:
            return None
        
        root = TreeNode(data)
        root.left = self.createTree()
        root.right = self.createTree()

        return root

    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    
    def preorder(self,root):
        if root is None:
            return
        
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def levelorder(self,root):
        if root is None:
            return
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            print(node.data, end=" ")
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)



BT = BinaryTree()
root = BT.createTree()

print("Inorder:", end=" ")
BT.inorder(root)
print()

print("Preorder:", end=" ")
BT.preorder(root)
print()

print("Postorder:", end=" ")
BT.postorder(root)
print()

print("Levelorder",end=" ")
BT.levelorder(root)
print()