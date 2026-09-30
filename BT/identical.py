# https://leetcode.com/problems/same-tree/
from typing import Optional,List

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
BT = BinaryTree()
p = BT.createTree(arr1)
sol = Solution()
q = BT.createTree(arr2)
print(sol.isSameTree(p,q))