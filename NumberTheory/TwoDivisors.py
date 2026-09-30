# https://codeforces.com/contest/1916/problem/B%C3%A2%C2%81%C2%A3
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
   def find_gcd(self,a:int, b:int) -> int:
       a  = abs(a)
       b = abs(b)
       if b == 0:
           return a
       return self.find_gcd(b,a%b)
   
   def Two_Divisors(self, a:int, b:int)->int:
       # b = a* prime number
       # x = b*p
       # x =  b * (prime number)/a
       if b%a == 0:
           return b *(b//a)
       return  a * (b//self.find_gcd(a,b))

sol = Solution()
t = int(input())
for _ in range(t):
    n1,n2 = map(int, input().split())
    print(sol.Two_Divisors(n1,n2))
