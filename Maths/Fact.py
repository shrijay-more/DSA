from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = (10**9)+7

    def calcFact(self,n:int):
        fact = [0] * (n+1)
        fact[0] =1
        for i in range(1,n+1):
            fact[i] = (fact[i-1] * i)% self.MOD

        return fact

sol = Solution()
t = int(input())

for _ in range(t):
    n =  int(input())
    print(sol.calcFact(n))