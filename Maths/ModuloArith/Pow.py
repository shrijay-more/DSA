# https://leetcode.com/problems/powx-n/description/
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow(x, -n)
        return self.pow(x, n)
    

    def binary_expo(self, a:int, n:int)->int:
        result = 1
        exp = abs(n)
        while exp > 0:
            if exp & 1:
                result *= a
            a *= a
            exp >>= 1 
        if n < 0:
            return 1 / result
        return result


sol = Solution()
t = int(input())
for _ in range(t):
    x = float(input())
    n = int(input())
    print(sol.myPow(x,n))
