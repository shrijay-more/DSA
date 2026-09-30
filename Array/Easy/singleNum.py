import sys
from typing import List

sys.stdin = open('z.txt','r')

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor^=nums[i]

        return xor

s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.singleNumber(arr))