# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        depth,maxi= 0,0
        for i in range(n):
            ch = s[i]
            if ch == '(':
                depth+=1
                maxi = max(depth,maxi)
            elif ch == ')':
                depth-=1

        return maxi

sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.maxDepth(s))