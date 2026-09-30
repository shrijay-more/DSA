# https://leetcode.com/problems/sort-colors/

from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def sortColors(self, nums:List[int])->None:
        n = len(nums)
        low,mid,high= 0,0,n-1

        while mid<=high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[high],nums[mid] = nums[mid],nums[high]
                high-=1
        


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.sortColors(arr)
    print(arr)