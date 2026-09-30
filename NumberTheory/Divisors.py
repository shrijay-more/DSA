import math
from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def divisors(self, num:int)->List[int]:
        ans = []
        n = int(math.sqrt(num))
        for i in range(1,n+1):
            if num % i == 0:
                ans.append(i)
                if i != (num//i):
                    ans.append(num//i)
        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.divisors(num))
