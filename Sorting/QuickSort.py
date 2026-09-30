from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def find_pivot(self, nums:List[int], low:int, high:int)-> None:
        i= low 
        j = high
        pivotEle = nums[low]
        while i<j:
            while i<=high and  nums[i] <= pivotEle:
                i+=1
            while j>=low and  nums[j] > pivotEle:
                j-=1  
            if i>=j:
                break
            else:
                nums[i],nums[j] = nums[j],nums[i]

        nums[low],nums[j] =  nums[j], nums[low]
        return j

    def quick_sort_helper(self, nums:List[int], low:int, high:int)->None:
        if low >= high:
            return
        pivot =  self.find_pivot(nums, low, high)
        self.quick_sort_helper(nums,low,pivot-1)
        self.quick_sort_helper(nums,pivot+1, high)

    def quick_sort(self,nums:List[int])->None:
        low = 0 
        high = len(nums)-1
        self.quick_sort_helper(nums, low,high)


s = Solution()
t = int(input())

for _ in range(t):
    n =  int(input())
    arr = list(map(int, input().split()))
    s.quick_sort(arr)
    print(arr)
