# https://leetcode.com/problems/maximum-product-subarray/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def maxProduct(self,nums:List[int])-> int:
        currMin, currMax = 1, 1
        res = max(nums)

        for num in nums:
            temp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            res = max(res, currMax)

        return res


s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.maxProduct(arr))
