from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def selection_sort(self,nums:List[int])->None:
        n = len(nums)
        for i in range(n):
            minInd = i
            for j in range(i+1,n):
                if nums[j] < nums[minInd]:
                    minInd = j
            
            nums[i], nums[minInd] = nums[minInd], nums[i]



    def find_min_index(self, nums:List[int], start:int, j:int, minInd:int)->int:
        if j > len(nums)-1:
            return minInd
        
        if nums[minInd] > nums[j]:
            minInd = j
        
        return self.find_min_index(nums,start, j+1, minInd)
        

    def selection_sort_helper(self, nums:List[int], start:int)->None:
        if start >= len(nums)-1:
            return
        
        minInd = self.find_min_index(nums,start, start+1, start)
        nums[start],nums[minInd] = nums[minInd],nums[start]
        self.selection_sort_helper(nums,start+1)


    def selection_sort_recursive(self, nums:List[int])->None:
        n = len(nums)
        self.selection_sort_helper(nums,0)



s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.selection_sort_recursive(arr)
    print(arr)
