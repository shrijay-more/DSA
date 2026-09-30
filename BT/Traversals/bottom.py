# https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
from queue import Queue
class BinaryTree:
    def __init__(self):
        self.idx = 0

    class TreeNode:
        def __init__(self,val):
            self.val = val
            self.left = None
            self.right = None

    
    def crateTree(self, arr):
        if self.idx >= len(arr):
            return None
        
        if arr[self.idx] == -1:
            self.idx+=1
            return None
        
        node = self.TreeNode(arr[self.idx])
        self.idx+=1

        node.left = self.crateTree(arr)
        node.right = self.crateTree(arr)

        return node


class Solution: 
    def __init__(self):
        pass

    def bottomView(self,root):
        if root is None:
            return None
        q = Queue()
        mpp = {}
        q.put((root,0))

        while not q.empty():
            node,col= q.get()
            mpp[col] = node.val

            if node.left:
                q.put((node.left, col-1))

            if node.right:
                q.put((node.right, col+1))

        
        ans = []
        
        for i in sorted(mpp.keys()):
            ans.append(mpp[i])

        return ans 

arr = list(map(int, input().split(" ")))
BT = BinaryTree()
sol = Solution()
root = BT.crateTree(arr)
print(sol.bottomView(root))