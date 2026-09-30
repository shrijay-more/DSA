# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional,List
class TreeNode:
    def __init__(self,data):
        self.data = data
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
    def findHeight(self,root:Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        return 1 + max(left,right)

    def findDiameter(self,root:Optional[TreeNode],maxi:List[int]) ->int:
        if root is None:
            return
        
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        maxi[0] = max(maxi[0], left+right)

        self.findDiameter(root.left,maxi)
        self.findDiameter(root.right,maxi)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]*1
        self.findDiameter(root,maxi)
        return maxi[0]
    
class SolutionOptimal:
    def findDiameter(self,root:Optional[TreeNode],maxi:List[int]) ->int:
        if root is None:
            return 0

        left= self.findDiameter(root.left,maxi)
        right= self.findDiameter(root.right,maxi)

        maxi[0] = max(maxi[0], left+right)

        return 1 + max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]*1
        self.findDiameter(root,maxi)
        return maxi[0]
        

arr =  list(map(int, input().split(" ")))
BT = BinaryTree()
sol = Solution()

root = BT.createTree(arr)
print(sol.diameterOfBinaryTree(root))
