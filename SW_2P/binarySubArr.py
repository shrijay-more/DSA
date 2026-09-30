# https://leetcode.com/problems/binary-subarrays-with-sum/
from typing import List

class Solution:
    def helper(self,nums:List[int], goal:int)->int:
        if goal < 0:
            return 0
        l,r,cnt,summ = 0,0,0,0
        n = len(nums)
        while r < n:
            summ+=nums[r]

            while summ > goal:
                summ-=nums[l]
                l+=1
            
            if summ <= goal:
                cnt+=(r-l+1)
            
            r+=1

        return cnt
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.helper(nums,goal) - self.helper(nums,goal-1) 
    
sol = Solution()

t = int(input())

for _ in range(t):
    goal = int(input())
    nums = list(map(int,input().split(" ")))
    print(sol.numSubarraysWithSum(nums, goal))