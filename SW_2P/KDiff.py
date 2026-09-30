# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
from typing import List
class Solution:
    def helper(sef, nums:List[int], k:int) ->int:
        if k < 0:
            return 0
        l,r,cnt= 0,0,0
        n = len(nums)
        mpp = {}
        while r < n :
            if nums[r]  not in mpp:
                mpp[nums[r]]=1
            else:
                mpp[nums[r]]+=1
            while len(mpp) > k:
                mpp[nums[l]]-=1
                if mpp[nums[l]] == 0:
                    del mpp[nums[l]]
                l+=1

            cnt += (r-l+1)

            r+=1
        
        return cnt

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k) - self.helper(nums,k-1)
        

sol = Solution()

t = int(input())

for _ in range(t):
    goal = int(input())
    nums = list(map(int,input().split(" ")))
    print(sol.subarraysWithKDistinct(nums, goal))