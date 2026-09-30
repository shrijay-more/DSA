# https://leetcode.com/problems/remove-outermost-parentheses/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        n = len(s)
        ans = ""
        for i in range(n):
            if s[i] == '(':
                if counter > 0:
                    ans+='('
                counter+=1
            else:
                counter-=1
                if counter > 0:
                    ans+=')'
        return ans
                
sol = Solution()

t = int(input())

for _ in range(t):
   s = str(input())
   print(sol.removeOuterParentheses(s))
    