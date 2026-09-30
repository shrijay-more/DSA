# https://leetcode.com/problems/symmetric-tree/ 

from typing import Optional

class TreeNode:
    def __init__(self,val):
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
            self.idx+=1
            return None
        
        node = TreeNode(arr[self.idx])
        self.idx+=1

        node.left = self.createTree(arr)
        node.right = self.createTree(arr)

        return node
    

class Solution:
    def isSymmetricHelper(self, left:Optional[TreeNode], right:Optional[TreeNode]) -> bool:
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetricHelper(left.left, right.right)  and self.isSymmetricHelper(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        return self.isSymmetricHelper(root.left, root.right)
   

BT = BinaryTree()
sol = Solution()
arr = list(map(int, input().split(" ")))
root = BT.createTree(arr)
print(sol.isSymmetric(root))