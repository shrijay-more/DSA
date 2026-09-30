# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List
import sys
sys.stdin = open('z.txt','r')
class Solution:
    def check(this, nums:List[int])-> bool:
        cnt = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                cnt = cnt+1
                if cnt > 1:
                    return False
        return True

s = Solution()

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.check(arr))