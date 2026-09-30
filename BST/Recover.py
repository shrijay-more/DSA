class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def buildBST(self, arr):
        root = None
        for val in arr:
            root = self.insert(root, val)
        return root


class Solution:
    def __init__(self):
        self.first = None
        self.prev = None
        self.middle = None
        self.last = None

    def inorder(self,root):
        if root is None:
            return

        self.inorder(root.left)
        if self.prev is not None and root.val < self.prev.val:
            if self.first is None:
                self.first= self.prev
                self.middle = root
            else:
                self.last = root

        self.prev = root
        self.inorder(root.right)

    def recoverTree(self,root):
        self.first,self.middle,self.last = None,None,None
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)
        if self.first and self.last:
            temp = self.first.val
            self.first.val = self.last.val
            self.last.val = temp
        elif self.first and self.middle:
            temp = self.first.val
            self.first.val = self.middle.val
            self.middle.val = temp