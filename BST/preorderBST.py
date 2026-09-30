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
    def BSTfromPreorder(self,arr):
        i = 0
        return self.build(arr,i,float('inf'))

    def build(self,arr,i,bound):
        if i == len(arr) or arr[i] > bound:
            return None

        root = TreeNode(arr[i])
        i+=1
        root.left = self.build(arr,i,root.val)
        root.right = self.build(arr,i,bound)
        return root
    