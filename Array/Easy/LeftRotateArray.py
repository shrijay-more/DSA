# https://leetcode.com/problems/rotate-array/description/
from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def rotate(self, nums:List[int], k:int)-> None:
        n = len(nums)
        k = k%n

        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


s = Solution()

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    s.rotate(arr,k)
    print(arr)
