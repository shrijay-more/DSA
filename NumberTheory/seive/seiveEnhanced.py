import math
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    # SPF : Smallest prime factor for number till num
    def SPF(self, num:int)->List[int]:
        spf=[0]*(num+1)
        
        for i in range(2,num+1):
            if spf[i] == 0:
                spf[i] = i
                for j in range(i*i, num+1,i):
                    if spf[j]==0:
                        spf[j]=i

        for i in range(len(spf)):
            print(spf[i],end=" ")
        print()

        return spf
    
    def BPF(self, num:int)->List[int]:
        bpf = [0] * (num + 1)
        
        for i in range(2, num + 1):
            if bpf[i] == 0:  # i is prime
                for j in range(i, num + 1, i):
                    bpf[j] = i 

        for i in range(len(bpf)):
            print(bpf[i],end=" ")
        print()
 
    # prime factorizing using spf
    def prime_factorization(self, k:int, spf:List[int])->None:
        prime_factors = []
        while k !=1 :
            prime_factors.append(spf[k])
            k=k//spf[k]
        
        for i in range(len(prime_factors)):
            print(prime_factors[i],end=" ")
        print()

    def sum_of_divisors(self,num:int)->None:
        sod = [0] * (num+1)
        for i in range(1,num+1):
            for j in range(i,num+1,i):
                sod[j]+=i

        print(sod)

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    #spf = sol.SPF(num)
    #sol.prime_factorization(12,spf)
    #sol.sum_of_divisors(num)
    sol.BPF(num)
    
