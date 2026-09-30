from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def missingNumber(self, nums:List[int])-> int:
        i = 0
        n = len(nums)
        while i < n:
            correctIndex = nums[i]
            if nums[i] < n and nums[i]!= nums[correctIndex] and i < n:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i=i+1 

        for j in range(len(nums)):
            if nums[j]!=j:
                return j
            
        return n
    

s = Solution()

t =  int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.missingNumber(arr))