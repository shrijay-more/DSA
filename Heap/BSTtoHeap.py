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

    def inorder(self, root, inorder):
        if root is None:
            return

        self.inorder(root.left, inorder)
        inorder.append(root.val)
        self.inorder(root.right, inorder)

    def preorder_fill(self, root, inorder, index):
        if root is None:
            return index

        root.val = inorder[index]
        index += 1

        index = self.preorder_fill(root.left, inorder, index)
        index = self.preorder_fill(root.right, inorder, index)

        return index

    def preorder(self, root):
        if root is None:
            return

        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


BST = BinarySearchTree()

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    root = BST.buildBST(arr)

    inorder = []
    BST.inorder(root, inorder)

    BST.preorder_fill(root, inorder, 0)

    BST.preorder(root)
    print()