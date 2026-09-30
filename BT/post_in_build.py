
from typing import Optional,List

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        indexMap = {val: i for i, val in enumerate(inorder)}

        def helper(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            # Last element of postorder is the root
            rootVal = postorder[postEnd]
            root = TreeNode(rootVal)

            # Index of root in inorder
            index = indexMap[rootVal]

            # Number of nodes in left subtree
            leftSize = index - inStart

            # Build left subtree
            root.left = helper(
                inStart,
                index - 1,
                postStart,
                postStart + leftSize - 1
            )

            # Build right subtree
            root.right = helper(
                index + 1,
                inEnd,
                postStart + leftSize,
                postEnd - 1
            )

            return root

        return helper(
            0,
            len(inorder) - 1,
            0,
            len(postorder) - 1
        )