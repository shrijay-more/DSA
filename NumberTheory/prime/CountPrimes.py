# https://leetcode.com/problems/count-primes/submissions/1969350387/
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2 :
            return 0
        seive = [1]*(n)
        seive[0],seive[1] = 0,0
        i = 2
        while i*i <n:
            if seive[i]:
                j = i*i
                while j < n:
                    seive[j] = 0
                    j+=i
            i+=1
        
        return sum(seive)


sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.countPrimes(num))
