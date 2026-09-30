from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def my_pow(self, a:int, n:int)->int:
        MOD = (10**9) + 7
        result = 1
        a = a % MOD
        while n > 0:
            if (n & 1):
                result = (result*a) % MOD
            a = (a*a) % MOD
            n= n>>1
        return result

    def countGoodNumbers(self, n: int) -> int:
        MOD= (10**9)+7
        evenCount = (n+1)//2
        oddCount = n//2
        ans = (self.my_pow(5, evenCount) * self.my_pow(4,oddCount)) % MOD
        return ans % MOD

sol =  Solution()

t = int(input())

for _ in range(t):
    n = int(input())
    print(sol.countGoodNumbers(n))