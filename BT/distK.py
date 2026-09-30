# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import Optional,List
from queue import Queue
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
    def markParents(self, root, parent):
        q = Queue()
        q.put(root)
        parent[root] = None

        while not q.empty():
            node = q.get()

            if node.left:
                parent[node.left] = node
                q.put(node.left)

            if node.right:
                parent[node.right] = node
                q.put(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        self.markParents(root, parent)

        visited = {}
        q = Queue()

        q.put(target)
        visited[target] = True

        level = 0

        while not q.empty():
            if level == k:
                break
            n = q.qsize()
            for _ in range(n):
                node = q.get()

                if node.left and node.left not in visited:
                    visited[node.left] = True
                    q.put(node.left)

                if node.right and node.right not in visited:
                    visited[node.right] = True
                    q.put(node.right)

                if parent[node] and parent[node] not in visited:
                    visited[parent[node]] = True
                    q.put(parent[node])

            level += 1

        ans = []

        while not q.empty():
            ans.append(q.get().val)

        return ans
    
BT = BinaryTree()
sol = Solution()

t = int(input())

for i in range(t):
    arr = list(map(int, input().split(" ")))
    root = BT.createTree(arr)
    target = root.left
    ans = sol.distanceK(root, target)
    print(ans)