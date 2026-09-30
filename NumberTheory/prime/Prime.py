import math
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def is_prime(self,num:int)->bool:
        if num < 2 :
            return False
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i+=1
        return True
    
    def prime_factorization(self, num:int)->List[int]:
        ans = []
        if num < 2:
            return ans
        i = 2
        while i*i <= num:
            while num%i == 0:
                ans.append(i)
                num//=i
            i+=1
        
        if num > 1:
            ans.append(num)
        return ans
    
    
    
sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    # print(sol.is_prime(num))
    print(sol.prime_factorization(num))
