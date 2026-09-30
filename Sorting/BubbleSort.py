from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def bubble_sort(self, nums:List[int]):
        n = len(nums)
        for i in range(n):
            flag = False
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1],nums[j]
                    flag = True

            if flag == False:
                break

    def bubble_sort_swap(self, nums:List[int], i:int, j:int)->None:
        if j >= len(nums)-i-1:
            return
        
        if nums[j] > nums[j+1]:
             nums[j], nums[j+1] = nums[j+1],nums[j]
           
        self.bubble_sort_swap(nums,i,j+1)

    def bubble_sort_helper(self, nums:List[int], i:int)->None:
        if i >= len(nums)-1 :
            return
        self.bubble_sort_swap(nums,i,0)
        self.bubble_sort_helper(nums,i+1)

    
    def bubble_sort_recursive(self, nums:List[int]):
        self.bubble_sort_helper(nums,0)
         

s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.bubble_sort_recursive(arr)
    print(arr)