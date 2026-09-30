# https://leetcode.com/problems/count-number-of-nice-subarrays/
from typing import List
class Solution:
    def helper(self,nums:List[int], goal:int)->int:
        if goal < 0:
            return 0
        l,r,cnt,summ = 0,0,0,0
        n = len(nums)
        while r < n:
            summ +=(nums[r]%2)

            while summ > goal:
                summ-=(nums[l]%2)
                l+=1
            
            if summ <= goal:
                cnt+=(r-l+1)
            
            r+=1

        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k) - self.helper(nums,k-1)


sol = Solution()

t = int(input())

for _ in range(t):
    goal = int(input())
    nums = list(map(int,input().split(" ")))
    print(sol.numberOfSubarrays(nums, goal))