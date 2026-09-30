from queue import Queue


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
    
class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        s = ""
        q = Queue()
        q.put(root)
        while not q.empty():
            currNode = q.get()
            if currNode is None:
                s+="#,"
            else:
                s+=str(currNode.val)+","

            if currNode is not None:
                q.put(currNode.left)
                q.put(currNode.right)
            
        return s
        

    def deserialize(self, data):
        if data == "":
            return None

        values = data.split(",")
        q = Queue()
        root = TreeNode(int(values[0]))
        i = 1
        q.put(root)
        while not q.empty():
            node = q.get()

            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.put(node.left)

            i+=1

            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.put(node.right)

            i+=1

        return root