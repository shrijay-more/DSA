# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
    
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        ans = []
        q = Queue()
        q.put(root)
        leftToRight = True

        while not q.empty():
            size = q.qsize()
            temp = [0] * size

            for i in range(size):
                node = q.get()

                index = i if leftToRight else size - 1 - i
                temp[index] = node.val

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)

            ans.append(temp)
            leftToRight = not leftToRight

        return ans
    
arr =  list(map(int, input().split(" ")))
BT = BinaryTree()
sol = Solution()

root = BT.createTree(arr)
print(sol.zigzagLevelOrder(root))