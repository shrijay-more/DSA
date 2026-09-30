from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    # perfect square always have odd number of divisors
    def no_of_divisors(self, num:int)->int:
        i = 1
        cnt = 0
        while i*i <= num:
            if num%i == 0:
                cnt+=1
                if i != (num//i):
                    cnt+=1
            i+=1

        return cnt
    
    # Prime factorization method
    def no_of_divisorsOptimal(self, num:int)->int:
        n = num 
        spf = [0] * (n + 1)

        for i in range(2, n + 1):
            if spf[i] == 0:
                for j in range(i, n + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

        res = 1
        while num > 1:
            prime = spf[num]
            count = 0
            
            while num % prime == 0:
                num //= prime
                count += 1

            res *= (count + 1)

        return res
                    

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.no_of_divisorsOptimal(num))
