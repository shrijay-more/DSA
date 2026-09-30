from queue import Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.idx = 0

    def createTree(self, arr):
        if self.idx >= len(arr):
            return None
        
        if arr[self.idx] == -1:
            self.idx += 1
            return None

        node = TreeNode(arr[self.idx])
        self.idx += 1

        node.left = self.createTree(arr)
        node.right = self.createTree(arr)

        return node
    
class Solution:
    def __init__(self):
        pass

    def topView(self,root):
        if root is None:
            return []
        
        ans = []
        q = Queue()
        q.put((root,0))
        mpp = {}
        while not q.empty():
            node,col = q.get()

            if col not in mpp:
                mpp[col] = node.val

            if node.left:
                q.put((node.left,col-1))
            if node.right:
                q.put((node.right,col+1))

        for col in sorted(mpp.keys()):
            ans.append(mpp[col])

        return ans
    

arr = list(map(int, input().split()))

BT = BinaryTree()
root = BT.createTree(arr)

sol = Solution()
print(sol.topView(root))