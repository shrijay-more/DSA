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
    def morris_inorder(self,root):
        inorder = []
        curr = root
        while curr is not None:
            if curr.left is None:
                inorder.append(curr.val)
                curr = curr.right

            else:
                prev = curr.left
                while prev.right and prev.right is not curr:
                    prev = prev.right

                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right

        return inorder
    def morris_preorder(self,root):
            preorder = []
            curr = root
            while curr is not None:
                if curr.left is None:
                    preorder.append(curr.val)
                    curr = curr.right
    
                else:
                    prev = curr.left
                    while prev.right and prev.right is not curr:
                        prev = prev.right
    
                    if prev.right is None:
                        prev.right = curr
                        preorder.append(curr.val)
                        curr = curr.left
                    else:
                        prev.right = None
                        curr = curr.right


    

