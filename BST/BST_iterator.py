class BST_Iterator:
    def __init__(self,root):
        self.mySt = []
        self.pushAll(root)

    def hasNext(self):
        return len(self.mySt) != 0

    def next(self):
        temp = self.mySt[-1]
        self.mySt.pop()
        self.pushAll(temp.right)
        return temp.val
    
    def pushAll(self,node):
        while node is not None:
            self.mySt.append(node)
            node = node.left
