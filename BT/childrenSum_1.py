# https://www.geeksforgeeks.org/problems/children-sum-parent/1
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
    def isSumPropertyHelper(self, root):
        if root is None:
            return True
            
        if root.left is None and root.right is None:
            return True
            
        left = root.left.val if root.left else 0
        right = root.right.val if root.right else 0
        
        if root.val != left + right:
            return False
            
        return (self.isSumPropertyHelper(root.left) and self.isSumPropertyHelper(root.right))
    
    def isSumProperty(self, root):
        return self.isSumPropertyHelper(root)
        