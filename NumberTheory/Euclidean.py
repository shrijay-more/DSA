from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def findGCD(self,a:int, b:int) -> int:
        mini = min(a,b)
        for i in range(mini, 0,-1):
            if a%i == 0 and b%i == 0:
                return i      
            
    def GCD_Optimal(self, a:int, b:int) ->int:
         a = abs(a)
         b = abs(b)
         if b == 0:
             return a
         return self.GCD_Optimal(b, a%b)
    
    def LCM_Optimal(self,a:int, b:int) ->int:
        return a // self.GCD_Optimal(a,b)*b
    
sol = Solution()
t = int(input())

for _ in range(t):
    n1,n2 =map(int, input().split())
    print(sol.GCD_Optimal(n1,n2))
    print(sol.LCM_Optimal(n1,n2))
    