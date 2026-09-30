from queue import Queue
from typing import Optional,List
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.idx = 0

    def createTree(self, arr):
        if self.idx >= len(arr):
            return None
        
        if arr[self.idx] == -1:
            self.idx+=1
            return None
        
        node = TreeNode(arr[self.idx])
        self.idx+=1
        node.left = self.createTree(arr)
        node.right = self.createTree(arr)

        return node
    

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q =  Queue()
        q.put(root)
        ans = []
        while not q.empty():
            length = q.qsize()

            for i in range(length):
                node = q.get()

                if i == length - 1:
                    ans.append(node.val)

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)


        return ans
    

arr = list(map(int, input().split(" ")))
BT = BinaryTree()
root = BT.createTree(arr)
sol = Solution()

print(sol.rightSideView(root))