# https://codeforces.com/problemset/problem/26/A%C3%A2%C2%81%C2%A3
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def AlmostPrime(self, num:int)->int:
        seive = [0]*(num+1)
        i = 2
        while i <= num:
            if seive[i] == 0:
                j = i
                while j<=num:
                    seive[j]+=1
                    j+=i
            i+=1

        cnt = 0
        for i in range(len(seive)):
            if seive[i] == 2:
                cnt+=1

        return cnt


sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.AlmostPrime(num))
