# https://codeforces.com/contest/57/problem/C%C3%A2%C2%81%C2%A3
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = (10**9) + 7
        self.MAXN =(10**5)
        self.fact = [0] * (self.MAXN + 1)
        self.invFact = [0] * (self.MAXN + 1)
        self.precompute()

    def modPow(self, base, exponent):
        res = 1
        while exponent > 0:
            if exponent & 1:
                res = (res * base) % self.MOD
            base = (base * base) % self.MOD
            exponent >>= 1
        return res

    def precompute(self):
        self.fact[0] = 1
        for i in range(1, self.MAXN + 1):
            self.fact[i] = (self.fact[i - 1] * i) % self.MOD

        self.invFact[self.MAXN] = self.modPow(self.fact[self.MAXN], self.MOD - 2)

        for i in range(self.MAXN, 0, -1):
            self.invFact[i - 1] = (self.invFact[i] * i) % self.MOD

    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.invFact[r] % self.MOD * self.invFact[n - r] % self.MOD

    def array(self, n):
        non_decreasing = self.nCr(2 * n - 1, n - 1)
        ans = (2 * non_decreasing - n) % self.MOD
        return ans


sol = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    print(sol.array(n))