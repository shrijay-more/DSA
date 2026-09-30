# https://leetcode.com/problems/max-consecutive-ones/description/
from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def findMaxConsecutiveOnes(self, nums:List[int])-> int:
        maxCount,count = 0,0
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=1
            else:
                maxCount = max(maxCount,count)
                count =0
        
        return max(maxCount,count)


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.findMaxConsecutiveOnes(arr))