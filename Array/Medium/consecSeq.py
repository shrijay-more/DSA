# https://leetcode.com/problems/longest-consecutive-sequence/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def longestConsecutiveBrute(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        maxCnt = 1
        for i in range(n):
            cnt = 1
            num = nums[i]
            found = True
            while found:
                found = False
                for j in range(n):
                    if nums[j] == num + 1:
                        num += 1
                        cnt += 1
                        found = True
                        break
            
            maxCnt = max(maxCnt, cnt)
        
        return maxCnt
    
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length+=1
                longest = max(longest,length)

        return longest

s= Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.longestConsecutiveBrute(arr))