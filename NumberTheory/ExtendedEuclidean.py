from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def extended_gcd(self,a:int, b:int):
        if b == 0:
            return a, 1, 0   # gcd, x, y
        gcd, x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

sol = Solution()
t = int(input())
for _ in range(t):
    n1,n2 = map(int, input().split())
    print(sol.extended_gcd(n1,n2))
    
