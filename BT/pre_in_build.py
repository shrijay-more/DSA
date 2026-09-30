# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def getIndex(self, arr:List[int], target) -> int:
        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return -1

    def buildTreeHelper(self, preorder:List[int], inorder:List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index =  self.getIndex(inorder,preorder[0])
        root.left = self.buildTreeHelper(preorder[1:index+1],inorder[:index])
        root.right = self.buildTreeHelper(preorder[index+1:], inorder[index+1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder,inorder)