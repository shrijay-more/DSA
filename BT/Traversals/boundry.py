class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.idx = 0

    def createTree(self, arr):
        if self.idx >= len(arr):
            return None

        if arr[self.idx] == -1:
            self.idx += 1
            return None

        node = TreeNode(arr[self.idx])
        self.idx += 1

        node.left = self.createTree(arr)
        node.right = self.createTree(arr)

        return node


class Solution:

    def isLeaf(self, root):
        return root.left is None and root.right is None

    def addLeftBoundary(self, root, res):
        node = root.left

        while node:
            if not self.isLeaf(node):
                res.append(node.val)

            if node.left:
                node = node.left
            else:
                node = node.right

    def addLeafNodes(self, root, res):
        if root is None:
            return

        if self.isLeaf(root):
            res.append(root.val)
            return

        self.addLeafNodes(root.left, res)
        self.addLeafNodes(root.right, res)

    def addRightBoundary(self, root, res):
        node = root.right
        temp = []

        while node:
            if not self.isLeaf(node):
                temp.append(node.val)

            if node.right:
                node = node.right
            else:
                node = node.left

        while temp:
            res.append(temp.pop())

    def boundaryTraversal(self, root):
        if root is None:
            return []

        if self.isLeaf(root):
            return [root.val]

        res = [root.val]

        self.addLeftBoundary(root, res)
        self.addLeafNodes(root, res)
        self.addRightBoundary(root, res)

        return res



arr = list(map(int, input().split()))

BT = BinaryTree()
root = BT.createTree(arr)

sol = Solution()

print("Boundary Traversal:")
print(sol.boundaryTraversal(root))