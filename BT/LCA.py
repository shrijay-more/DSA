# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root ==p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

def findNode(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    left = findNode(root.left, val)
    if left:
        return left

    return findNode(root.right, val)   

BT = BinaryTree()
sol = Solution()

t = int(input)

for _ in range(t):
    arr = list(map(int, input().split()))
    root = BT.createTree(arr)

    i, j = map(int, input().split())

    p = findNode(root, arr[i])
    q = findNode(root, arr[j])

    ans = sol.lowestCommonAncestor(root, p, q)
    print(ans.val if ans else -1)