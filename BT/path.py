class TreeNode:
    def __init__(self,data):
        self.data = data
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
    def findPathHelper(self, root, value, ans):
        if root is None:
            return False

        ans.append(root.data)
        
        if root.data == value:
            return True

        if (self.findPathHelper(root.left, value, ans) or
                self.findPathHelper(root.right, value, ans)):
            return True

        ans.pop()
        return False

    def findPath(self, root, value):
        if root is None:
            return []

        ans = []
        self.findPathHelper(root, value, ans)
        return ans
    

BT = BinaryTree()
sol = Solution()

t = int(input())

for _ in range(t):
    value = int(input())
    arr = list(map(int, input().split(" ")))
    root = BT.createTree(arr)
    print(sol.findPath(root,value))
