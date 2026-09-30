# https://codeforces.com/contest/2125/problem/B%C3%A2%C2%81%C2
import sys
from typing import List

sys.stdin = open('z.txt','r')

class Solution:
    def find_gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.find_gcd(b, a % b)
    
    def solve(self, a: int, b: int, k: int) -> int:
        g = self.find_gcd(a, b)
        if max(a // g, b // g) <= k:
            return 1
        else:
            return 2
    

sol = Solution()
t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    print(sol.solve(a, b, k))