# https://codeforces.com/contest/1203/problem/C%C3%A2%C2%81%C2%A3
import sys
from typing import List

sys.stdin = open('z.txt','r')

class Solution:
    def find_gcd(self, a:int,b:int) ->int:
        if b == 0:
            return a
        return self.find_gcd(b,a%b)
    
    def common_divisors(self,nums:List[int]) ->int:
        n = len(nums)
        gcd = nums[0]
        for num in nums[1:]:
            gcd = self.find_gcd(gcd,num)

        cnt = 0
        ans = 1
        i = 2
        while i*i <= gcd:
            cnt = 0
            while(gcd % i == 0):
                gcd = gcd//i
                cnt+=1
            ans = ans * (cnt+1)
            i+=1
        if gcd > 1:
            ans*=2

        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol.common_divisors(arr))
