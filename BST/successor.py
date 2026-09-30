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
    def inorder_sucessor(self,root,p):
        sucessor = None

        while root is not None:
            if p.val >= root.val:
                root = root.right
            else:
                sucessor = root
                root = root.left

        return sucessor
