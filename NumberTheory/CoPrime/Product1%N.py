# https://codeforces.com/problemset/problem/1514/C%C3%A2%C2%81%C2%A3

from math import gcd
import sys

sys.stdin = open('z.txt', 'r')

class Solution:
    def Product1ModuloN(self, n: int):
        res = []
        prod = 1
        # Step 1: collect coprimes
        for i in range(1, n):
            if gcd(i, n) == 1:
                res.append(i)
                prod = (prod * i) % n

        # Step 2: if product != 1, remove that element
        if prod != 1:
            res.remove(prod)

        print(len(res))
        print(*res)


sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    sol.Product1ModuloN(n)