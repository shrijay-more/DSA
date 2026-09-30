# https://leetcode.com/problems/sort-colors/

from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
     def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt , i = 0 ,0 
        num = -1
        while i < n :
            if cnt == 0:
                num = nums[i]
                i+=1
                cnt+=1
            elif num != nums[i]:
                cnt-=1
                i+=1
            else:
                i+=1
                cnt+=1

        return num


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.majorityElement(arr))