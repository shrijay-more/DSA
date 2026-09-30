# https://leetcode.com/problems/fruit-into-baskets/
from typing import List

class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        l,r,maxLen = 0,0,0
        mpp = {}
        n = len(nums)

        while r < n:
            if nums[r] not in mpp:
                mpp[nums[r]] = 1
            elif nums[r] in mpp:
                mpp[nums[r]]+=1
            
            if len(mpp) > 2:
                while len(mpp) >2:
                    mpp[nums[l]]-=1
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]

                    l+=1
            
            if len(mpp) <=2:
                maxLen = max(maxLen, r - l +1)
            
            r+=1
        
        return maxLen


t = int(input())
sol = Solution()
for _ in range(t):
    nums = list(map(int , input().split(" ")))
    print(sol.totalFruit(nums))