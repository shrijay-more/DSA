import math
from typing import List
import sys

sys.stdin = open('z.txt', 'r')

class Solution:
    def build_spf(self, MAXI):
        spf = [0] * (MAXI + 1)
        for i in range(2, MAXI + 1):
            if spf[i] == 0:
                for j in range(i, MAXI + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
        return spf

    def TPrimes(self, nums: List[int]) -> None:
        MAXI = max(nums)
        spf = self.build_spf(MAXI)
        for n in nums:
            temp = n
            factors = 1
            while temp > 1:
                prime = spf[temp]
                alpha = 0
                while temp % prime == 0:
                    temp //= prime
                    alpha += 1

                factors *= (alpha + 1)

            if factors == 3:
                print("YES")
            else:
                print("NO")

    def TPrimesOptimal(self,nums:List[int]) ->None:
        MAXI = 10**6
        seive = [1]*(MAXI+1)
        seive[0],seive[1] = 0,0
        i = 2
        while i*i <= MAXI:
            if seive[i]:
                for j in range(i*i,MAXI+1,i):
                    seive[j] = 0
            i+=1
        
        for n in nums:
            root = math.isqrt(n)
            if root * root == n and seive[root]:
                print("YES")
            else:
                print("No")
    
sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    arr = list(map(int, input().split()))
    sol.TPrimesOptimal(arr)