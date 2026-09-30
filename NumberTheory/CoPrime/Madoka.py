# https://codeforces.com/contest/1717/problem/E%C3%A2%C2%81%C2%A3
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def Madoka(self,num:int) ->int:
        ans = 0

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.Madoka(num))
