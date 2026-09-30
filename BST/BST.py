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

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def ceilHelper(self, root, val, ans):
        if root is None:
            return

        if root.val == val:
            ans[0] = root.val
            return

        if root.val > val:
            if ans[0] == -1 or root.val < ans[0]:
                ans[0] = root.val
            self.ceilHelper(root.left, val, ans)
        else:
            self.ceilHelper(root.right, val, ans)

    def ceil(self, root, val):
        ans = [-1]
        self.ceilHelper(root, val, ans)
        return ans[0]

    def floorHelper(self, root, val, ans):
        if root is None:
            return

        if root.val == val:
            ans[0] = root.val
            return

        if root.val < val:
            if ans[0] == -1 or root.val > ans[0]:
                ans[0] = root.val
            self.floorHelper(root.right, val, ans)
        else:
            self.floorHelper(root.left, val, ans)

    def floor(self, root, val):
        ans = [-1]
        self.floorHelper(root, val, ans)
        return ans[0]


    def helper(self,root:Optional[TreeNode],low:int, high:int) ->bool:
        if root is None:
            return True

        if root.val <= low or root.val >= high:
            return False
        
        return (self.helper(root.left,low,root.val) and self.helper(root.right,root.val,high))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,float('-inf'),float('inf'))


BST = BinarySearchTree()

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    root = BST.buildBST(arr)

    BST.inorder(root)
    print()

    x = int(input())

    print("Search:", BST.searchBST(root, x))
    print("Floor:", BST.floor(root, x))
    print("Ceil:", BST.ceil(root, x))