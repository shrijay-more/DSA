# https://leetcode.com/problems/max-consecutive-ones-iii/
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r,maxLen,zeros  = 0,0,0,0

        for i in range(n):
            if nums[i] == 0:
                zeros+=1

            if zeros > k:
                if nums[l] == 0:
                    zeros-=1
                l+=1

            if zeros <= k:
                maxLen = max (maxLen, r-l+1)

            r+=1

        return maxLen
            

t  = int(input())
sol  = Solution()
for _ in range(t):
    nums = list(map(int, input().split(" ")))
    print(sol.longestOnes(nums))
    