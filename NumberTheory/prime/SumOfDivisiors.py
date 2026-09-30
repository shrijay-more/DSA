from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def SumOfDivisors(self, num:int) ->int:
        ans = 0
        i = 1
        while i*i <= num:
            if num % i == 0:
                ans+=i
                if i != (num//i):
                    ans = ans + (num//i)
            i+=1
        ans-=num
        return ans
    
    def SumOfDivisorsOptimal(self, num:int) -> int:
        n = num
        MAXN = 10**5
        spf= [0] *(MAXN+1)
        for i in range(2,MAXN+1):
            if spf[i] == 0:
                for j in range(i, MAXN+1,i):
                    if spf[j] == 0:
                        spf[j] = i
        
        ans = 1
        while n > 1:
            prime = spf[n]
            power =1
            term =1
            while n%prime == 0:
                n = n//prime
                power*=prime
                term+=power
            ans*=term

        return ans - num


sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.SumOfDivisorsOptimal(num))
    
