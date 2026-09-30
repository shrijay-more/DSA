# http://leetcode.com/problems/string-to-integer-atoi/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def myAtoi(self, s:str)->int:
        s = s.strip()
        if not s:
            return 0
        i = 0
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        num = 0
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1
            
        return sign * num
    
sol  = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.myAtoi(s))