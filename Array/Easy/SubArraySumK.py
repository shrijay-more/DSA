from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def longestSubarry(self,nums,k)->int:
        my_map = {}
        ans,prefixSum = 0,0

        for i in range(len(nums)):
            prefixSum+=nums[i]
            if prefixSum == k:
                ans = i+1
        
            if (prefixSum-k) in my_map:
                ans = max(ans, i- my_map[prefixSum-k])

            if prefixSum not in my_map:
                my_map[prefixSum] = i

        return ans


s =  Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(s.longestSubarry(arr,k))
