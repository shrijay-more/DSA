# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

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
    def insertHelper(self,root:Optional[TreeNode], val:int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
            
        if root.val > val:
            root.left = self.insertHelper(root.left,val)
        else:
            root.right = self.insertHelper(root.right,val)

        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insertHelper(root,val)


    def findLastRight(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.right is None:
            return root

        return self.findLastRight(root.right)

    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        rightChild = root.right
        lastRight = self.findLastRight(root.left)
        lastRight.right = rightChild

        return root.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root

        while root is not None:
            if key < root.val:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy