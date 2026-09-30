# https://leetcode.com/problems/maximum-width-of-binary-tree/
from queue import Queue
from typing import Optional

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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        q = Queue()
        q.put((root, 0))

        while not q.empty():
            n = q.qsize()
            mini = q.queue[0][1]   # index of first node in this level

            first = last = 0

            for i in range(n):
                node, idx = q.get()
                curr_id = idx - mini

                if i == 0:
                    first = curr_id
                if i == n - 1:
                    last = curr_id

                if node.left:
                    q.put((node.left, 2 * curr_id + 1))
                if node.right:
                    q.put((node.right, 2 * curr_id + 2))

            ans = max(ans, last - first + 1)

        return ans