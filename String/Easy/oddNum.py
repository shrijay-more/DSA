# https://leetcode.com/problems/largest-odd-number-in-string/submissions/1966750659/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def largestOddNumber(self, num:str)->str:
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
            
        return ""


sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.largestOddNumber(s))

