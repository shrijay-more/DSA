# https://leetcode.com/problems/move-zeroes/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def moveZeroes(self, nums:List[int])-> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if(nums[j]!=0):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i=i+1


s = Solution()

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.moveZeroes(arr)
    print(arr)