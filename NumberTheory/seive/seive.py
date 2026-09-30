import math
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def seive(self, num:int)->None:
        prime = [1]*(num+1)
        prime[0],prime[1] = 0,0
        for i in range (2,num+1):
            if prime[i]:
                j = 2*i
                while j<=num:
                    prime[j] = 0
                    j+=i

        for i in range(len(prime)):
            if prime[i]!=0:
                print(i,end=" ")
        print()

    def seiveOptimized(self,num:int)->None:
        prime = [1]*(num+1)
        prime[0],prime[1] = 0,0
        # start from i*i because smaller indices are marked by smaller primes
        for i in range(2,num+1):
            if prime[i]:
                j = i*i
                while j<=num:
                    prime[j] = 0
                    j+=i

        for i in range(len(prime)):
            if prime[i]!=0:
                print(i,end=" ")
        print()

    def seiveOptimizedSqrt(self,num:int)->None:
        prime = [1]*(num+1)
        prime[0],prime[1] = 0,0
        i = 2
        # Go till sqrt of n only cause rest are automatically marked
        while i*i <= num:
            if prime[i]:
                j = i*i
                while j<=num:
                    prime[j]=0
                    j+=i
            i+=1

        for i in range(len(prime)):
            if prime[i]!=0:
                print(i,end=" ")
        print()

    def seiveOptimizedOdd(self, num: int) -> None:
        prime = [1] * (num + 1)
        prime[0], prime[1] = 0, 0

        # mark even numbers
        for i in range(4, num + 1, 2):
            prime[i] = 0

        i = 3
        while i * i <= num:
            if prime[i]:
                j = i * i
                while j <= num:
                    prime[j] = 0
                    j += 2 * i   # skip even multiples (important)
            i += 2   # 🔥 fix here

        print(2, end=" ")
        for i in range(3, num + 1, 2):
            if prime[i]:
                print(i, end=" ")
        print()

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    sol.seiveOptimizedOdd(num)
