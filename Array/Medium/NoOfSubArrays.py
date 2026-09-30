# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List
import sys

sys.stdin = open('z.txt','r')
class Solution:
     def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        map = dict()
        n = len(nums)
        prefixSum = 0
        map[0]=1
        for i in range(n):
            prefixSum+=nums[i]

            if prefixSum - k in map:
                cnt+=map[prefixSum-k]

            if prefixSum in map:
                map[prefixSum]+=1
            else:
                map[prefixSum]=1

        return cnt


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.subarraySum(arr))