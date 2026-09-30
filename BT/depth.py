# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
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
    def maxDepthHelper(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        
        left = 1 + self.maxDepthHelper(root.left)
        right = 1 + self.maxDepthHelper(root.right)

        return max(left,right)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)


arr = list(map(int, input().split(" ")))
BT = BinaryTree()
sol = Solution()
root = BT.createTree(arr)
print(sol.maxDepth(root))


    

