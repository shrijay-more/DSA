# https://leetcode.com/problems/roman-to-integer/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" :1,
            "V" :5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000
        }
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n-1 and values[s[i]] < values[s[i+1]]:
                ans+= (values[s[i+1]] - values[s[i]])
                i+=2
            else:
                ans+=values[s[i]]
                i+=1
        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.romanToInt(s))