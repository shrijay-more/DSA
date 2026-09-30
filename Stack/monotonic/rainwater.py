# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def prefixMax(self,nums:List[int]) -> int:
        n = len(nums)
        prefix = [0] * n

        prefix[0] = nums[0]
        for i in range(n):
            prefix[i] = max(prefix[i-1], nums[i])

        return prefix
    
    def suffixMax(self, nums:List[int]) ->int:
        n = len(nums)
        suffix = [0] * n
        suffix[n-1] = nums[n-1]

        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1], nums[i])

        return suffix
    
    def trap(self,heights:List[int])->int:
        ans = 0
        n = len(heights)
        suffix = self.suffixMax(heights)
        prefix = self.prefixMax(heights)

        for i in range(n):
            leftMax = prefix[i]
            rightMax = suffix[i]

            if heights[i] < leftMax and heights[i] < rightMax:
                ans = ans + min(leftMax,rightMax) - heights[i]
            
        return ans


sol = Solution()
t = int(input())

for _ in range(t):
    heights = list(map(int, input().split(" ")))
    print(sol.trap(heights))
