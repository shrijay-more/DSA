# https://codeforces.com/contest/300/problem/C%C3%A2%C2%81%C2%A3%C3%A2%C2%81%C2%A3
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = (10**9)+7
        self.fact = []
        self.invFact = []

    def modPow(self, base, exponent):
        res = 1 % self.MOD
        while exponent > 0:
            if exponent & 1:
                res = (res * base) % self.MOD
            base = (base * base) % self.MOD
            exponent >>= 1
        return res
    
    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.invFact[r] % self.MOD * self.invFact[n-r] % self.MOD
    
    def isGood(self, x, a, b):
        while x > 0:
            d = x % 10
            if d != a and d != b:
                return False
            x //= 10
        return True

    def beautifulNumbers(self, a, b, n):
        self.fact = [0] * (n+1)
        self.invFact = [0] * (n+1)

        self.fact[0] = 1
        for i in range(1, n+1):
            self.fact[i] = (self.fact[i-1] * i) % self.MOD

        self.invFact[n] = self.modPow(self.fact[n], self.MOD-2)
        for i in range(n-1, -1, -1):
            self.invFact[i] = (self.invFact[i+1] * (i+1)) % self.MOD

        ans = 0
        for k in range(n+1):
            total = k*b + (n-k)*a
            if self.isGood(total, a, b):
                ans = (ans + self.nCr(n, k)) % self.MOD

        return ans
    

sol = Solution()
t = int(input())

for _ in range(t):
    a,b,n, =  map(int, input().split())
    print(sol.beautifulNumbers(a,b,n))