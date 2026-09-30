# https://leetcode.com/problems/super-pow/description/
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        if a == 1:
            return 1
        phi = 1140

        exponent = 0
        for digit in b:
            exponent = (exponent*10 + digit)%phi

        if exponent == 0:
            exponent = phi

        result = 1
        a%=MOD
        while exponent >  0 :
            if exponent % 2 == 1:
                result = (result*a)%MOD
            a = (a*a)%MOD
            exponent = exponent//2

        return result
    
sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    arr = list(map(int, input().split()))
    a = int(input())
    print(sol.superPow(a,arr))
