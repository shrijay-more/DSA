# https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def findTwoElement(self, nums):
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            correctIndex =  nums[i]-1
            if nums[i]!=nums[correctIndex]:
                nums[i],nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i+=1
                
        for i in range(n):
            if i != nums[i]-1:
                ans = [nums[i],i+1]

        return ans


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.findTwoElement(arr))