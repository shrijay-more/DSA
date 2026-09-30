from typing import List
import sys


sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = (10**9) + 7
    
    def modPow(self, a, b, MOD):
        res = 1 % MOD
        a = a % MOD
        while b > 0:
            if b & 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b >>= 1
        return res

    def exponentiation(self, a, b, c):
        exponent = self.modPow(b, c, self.MOD - 1)
        return self.modPow(a, exponent, self.MOD)

sol = Solution()
t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    print(sol.exponentiation(a,b,c))