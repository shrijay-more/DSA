from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    MOD = (10**9) + 7   # ✅ defined once

    def my_pow(self, base:int, exponent:int) -> int:
        res = 1 % self.MOD
        
        while exponent > 0:
            if exponent & 1:
                res = (res * base) % self.MOD
            base = (base * base) % self.MOD
            exponent >>= 1
        
        return res

    def magic_locker(self, n:int) -> int:
        if n <= 3:
            return n
        
        k_times = n // 3
        remainder = n % 3

        if remainder == 0:
            ans = self.my_pow(3, k_times)
        elif remainder == 1:
            ans = (self.my_pow(3, k_times - 1) * 4) % self.MOD
        else:
            ans = (self.my_pow(3, k_times) * 2) % self.MOD

        return ans % self.MOD


sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    print(sol.magic_locker(n))