# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
import sys

sys.stdin= open('z.txt','r')

class Solution:
    def maxProfit(self, nums:List[int])->int:
        bought = nums[0]
        ans = float('-inf')
        for i in range(len(nums)):
            if nums[i] < bought:
                bought = nums[i]
            else:
                ans = max(ans, nums[i]-bought)

        return ans


s = Solution()
t = int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    print(s.maxProfit(arr))