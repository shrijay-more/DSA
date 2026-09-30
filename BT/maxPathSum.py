# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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
    
from typing import Optional,List
class Solution:
    def maxPathSumHelper(self,root:Optional[TreeNode],maxi:List[int]) ->int:
        if root is None:
            return 0

        left = max(0, self.maxPathSumHelper(root.left, maxi))
        right = max(0, self.maxPathSumHelper(root.right, maxi))

        maxi[0] = max(maxi[0], left+right+root.val)

        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [float('-inf')]
        self.maxPathSumHelper(root,maxi)
        return maxi[0]
    
    
arr =  list(map(int, input().split(" ")))
BT = BinaryTree()
sol = Solution()
root = BT.createTree(arr)
print(sol.maxPathSum(arr))