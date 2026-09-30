from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def precompute(self)->List[int]:
        MAX = (10**6)*5
        phi = [0] * (MAX+1)
        for i in range(MAX+1):
            phi[i] = i

        for i in range(2,MAX+1):
            if phi[i] == i:
                phi[i] = i-1
                for j in range(2*i, MAX+1, i):
                    phi[j] = (phi[j]//i)*(i-1)
     
        return phi
    
    def Mathematically_hard(self,n1:int, n2:int)->int:
        phi = self.precompute()
        sum = 0 
        for i in range(n1,n2+1):
            sum+=phi[i]*phi[i]

        return sum

sol = Solution()
t = int(input())
for _ in range(t):
    n1,n2 = map(int,input().split())
    print(sol.Mathematically_hard(n1,n2))
