from typing import List
import sys

sys.stdin =  open('z.txt','r')

class Solution:
    def inertion_sort(self, nums:List[int])->None:
        n = len(nums)
        for i in range(n):
            j = i-1
            key = nums[i]
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key

    def insertion_sort_insert(self, nums:List[int], i:int, j:int, key:int)->None:
        if j< 0 or  nums[j] <= key:
            nums[j+1]= key 
            return
        
        nums[j+1] = nums[j]
        self.insertion_sort_insert(nums,i,j-1,key)

    def insertion_sort_helper(self, nums:List[int], i: int)->None:
        if i>= len(nums):
            return
        self.insertion_sort_insert(nums,i,i-1,nums[i])
        self.insertion_sort_helper(nums,i+1)

    def insertion_sort_recursive(self, nums:List[int])-> None:
        self.insertion_sort_helper(nums,1)


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.insertion_sort_recursive(arr)
    print(arr)