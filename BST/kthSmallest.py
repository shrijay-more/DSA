from typing import Optional,List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def buildBST(self, arr):
        root = None
        for val in arr:
            root = self.insert(root, val)
        return root
    
class Solution:
    def helper(self, root:Optional[TreeNode],k:int,cnt:List[int], ans:List[int])-> None:
        if root is None:
            return 
        
        self.helper(root.left, k,cnt,ans)
        cnt[0]+=1
        if cnt[0] == k:
            ans[0] = root.val
        self.helper(root.right,k,cnt,ans)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt= [0]
        ans = [-1]
        self.helper(root,k,cnt,ans)
        return ans[0]