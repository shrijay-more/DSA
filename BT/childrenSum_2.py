class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.idx = 0

    def createTree(self,arr):
        if self.idx >= len(arr):
            return None
        
        if arr[self.idx] == -1:
            self.idx+=1
            return
        
        node = TreeNode(arr[self.idx])
        self.idx+=1

        node.left = self.createTree(arr)
        node.right = self.createTree(arr)

        return node
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)


class Solution:
    def childrenSumProperty(self, root):
        if root is None:
            return
        
        child = 0
        if root.left:
            child+=root.left.val

        if root.right:
            child+=root.right.val

        if child >= root.val:
            root.data = child
        else:
            if root.left:
                root.left.val = root.val
            elif root.right:
                root.right.val = root.val

        self.childrenSumProperty(root.left)
        self.childrenSumProperty(root.right)

        total = 0
        if root.left:
            total+=root.left.val

        if root.right:
            total+=root.right.val

        if root.right or root.left:
            root.val = total
            
            

sol = Solution()
BT = BinaryTree()

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split(" ")))
    root = BT.createTree(arr)
    sol.childrenSumProperty(root)
    BT.inorder(root)