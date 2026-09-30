# https://www.geeksforgeeks.org/problems/burning-tree/1
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
    def markParents(self, root, parent, target):
        q = Queue()
        q.put(root)
        parent[root] = None
        targetNode = None
    
        while not q.empty():
            node = q.get()
    
            if node.data == target:
                targetNode = node
    
            if node.left:
                parent[node.left] = node
                q.put(node.left)
    
            if node.right:
                parent[node.right] = node
                q.put(node.right)
    
        return targetNode
        
    def minTime(self, root, target):
        parents = {}
        targetNode = self.markParents(root, parents, target)
        
        vis = {}
        q = Queue()
        
        q.put(targetNode)
        vis[targetNode] = True
        time = 0
        while not q.empty():
            size = q.qsize()
            burned = False
        
            for _ in range(size):
                node = q.get()
        
                if node.left and node.left not in vis:
                    vis[node.left] = True
                    q.put(node.left)
                    burned = True
        
                if node.right and node.right not in vis:
                    vis[node.right] = True
                    q.put(node.right)
                    burned = True
        
                if parents[node] and parents[node] not in vis:
                    vis[parents[node]] = True
                    q.put(parents[node])
                    burned = True
        
            if burned:
                time += 1
                
        return time
    

BT = BinaryTree()
sol = Solution()

t = int(input())

for i in range(t):
    arr = list(map(int, input().split(" ")))
    root = BT.createTree(arr)
    target = root.left
    ans = sol.minTime(root, target)
    print(ans)