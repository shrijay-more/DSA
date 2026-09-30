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
    def countNodes(self, root):
        if root is None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def isCBT(self, root, index, nodes):
        if root is None:
            return True

        if index >= nodes:
            return False

        left = self.isCBT(root.left, 2 * index + 1, nodes)
        right = self.isCBT(root.right, 2 * index + 2, nodes)

        return left and right

    def isMaxOrder(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.right is None:
            return root.val > root.left.val

        left = self.isMaxOrder(root.left)
        right = self.isMaxOrder(root.right)

        if (
            left
            and right
            and root.val > root.left.val
            and root.val > root.right.val
        ):
            return True

        return False

    def isHeap(self, root):
        totalCount = self.countNodes(root)

        if self.isCBT(root, 0, totalCount) and self.isMaxOrder(root):
            return True

        return False


BT = BinaryTree()
sol = Solution()

t = int(input())

for _ in range(t):
    BT.idx = 0
    arr = list(map(int, input().split()))
    root = BT.createTree(arr)
    print(sol.isHeap(root))