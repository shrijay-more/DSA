# https://leetcode.com/problems/count-complete-tree-nodes/

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
    def leftHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def rightHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height

    def countNodes(self, root):
        if not root:
            return 0

        lh = self.leftHeight(root)
        rh = self.rightHeight(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)