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

    def traversal(self, root):
        if root is None:
            return

        st = []
        st.append([root, 1])

        preorder = []
        inorder = []
        postorder = []

        while st:
            node, num = st[-1]
            
            if num == 1:
                preorder.append(node.val)
                st[-1][1] = 2

                if node.left:
                    st.append([node.left, 1])

            elif num == 2:
                inorder.append(node.val)
                st[-1][1] = 3
                if node.right:
                    st.append([node.right, 1])

            else:
                postorder.append(node.val)
                st.pop()

        print("Preorder :", preorder)
        print("Inorder  :", inorder)
        print("Postorder:", postorder)


arr = list(map(int, input().split()))

BT = BinaryTree()
root = BT.createTree(arr)
BT.traversal(root)