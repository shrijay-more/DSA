# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
from typing import List, Optional
from queue import Queue

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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = Queue()
        q.put((root, 0, 0))

        mpp = {}

        while not q.empty():
            node, col, row = q.get()
            if col not in mpp:
                mpp[col] = {}
                
            if row not in mpp[col]:
                mpp[col][row] = []

            mpp[col][row].append(node.val)

            if node.left:
                q.put((node.left, col - 1, row + 1))

            if node.right:
                q.put((node.right, col + 1, row + 1))

        ans = []

        for col in sorted(mpp.keys()):
            temp = []
            for row in sorted(mpp[col].keys()):
                temp.extend(sorted(mpp[col][row]))
            ans.append(temp)

        return ans
    

arr = list(map(int, input().split(" ")))
BT = BinaryTree()
root = BT.createTree(arr)
sol = Solution()
print(sol.verticalTraversal(root))