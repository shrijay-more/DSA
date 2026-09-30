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
    def LCA(self,root,p,q):
        if root is None:
            return None

        curr = root.val
        if curr < p.val and curr < q.val:
            return self.LCA(root.left,p,q)
        if curr > p.val and curr > q.val:
            return self.LCA(root.right,p,q)
        return root
