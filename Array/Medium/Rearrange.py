# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        ans = [0]*n
        evenIndex = 0
        oddIndex = 1
        for i in range(len(nums)):
            if nums[i] > 0 and evenIndex<n:
                ans[evenIndex] = nums[i]
                evenIndex+=2
            elif nums[i] < 0  and oddIndex <n:
                ans[oddIndex] = nums[i]
                oddIndex+=2
            
        return ans


s = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.rearrangeArray(arr))