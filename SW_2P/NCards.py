# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
from typing import List
class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        leftSum = 0
        rightSum = 0
        maxSum = 0
        for i in range(k):
            leftSum+=nums[i]
        
        maxSum = leftSum

        rightIndex = len(nums)-1

        for i in range(k-1,-1,-1):
            leftSum-=nums[i]
            rightSum+=nums[rightIndex]
            rightIndex-=1
            maxSum = max(maxSum, leftSum+rightSum)

        
        return maxSum

sol = Solution()
t = int(input())

for i in range(t):
    k = int(input())
    nums = list(map(int, input().split(" ")))
    print(sol.maxScore(nums,k))

