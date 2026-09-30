# https://leetcode.com/problems/maximum-subarray/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:

    def printMaxSubArray(self, nums:List[int])-> None:
        maxEnding = nums[0]
        res = nums[0]

        start = 0
        end = 0
        tempStart = 0

        for i in range(1, len(nums)):
            if maxEnding < 0:
                maxEnding = nums[i]
                tempStart = i  
            else:
                maxEnding += nums[i]

            if maxEnding > res:
                res = maxEnding
                start = tempStart
                end = i

        for i in range(start,end+1):
            print(nums[i], end=" ")
        


        
    def maxSubArray(self, nums:List[int])-> int :
        maxEnding = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res,maxEnding)

        return res



s = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(s.maxSubArray(arr))
    s.printMaxSubArray(arr)
    print()