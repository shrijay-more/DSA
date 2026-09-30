# https://leetcode.com/problems/balanced-binary-tree/description/
from typing import Optional

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
    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.isBalancedHelper(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.isBalancedHelper(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root) != -1