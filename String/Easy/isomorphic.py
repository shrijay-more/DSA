# https://leetcode.com/problems/isomorphic-strings/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def Isomorphic(self, s:str, t:str) -> bool:
        if len(s) > len(t):
            return False
        mapST, mapTS = {},{}

        for i in range(len(s)):
            c1, c2 = s[i],t[i]

            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else :
                mapST[c1] = c2
            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1
        return True

sol = Solution()
t = int(input())
for _ in range(t):
    s,t = map(str, input().split())
    print(sol.Isomorphic(s,t))
