# https://leetcode.com/problems/rotate-string/submissions/1967775766/
from typing import List
import sys

sys.stdin = open('z.txt','r')
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s = s+s
        if goal in s:
            return True
        else:
            return False


sol = Solution()
t = int(input())
for _ in range(t): 
    s, goal =  map(str, input().split())
    print(sol.rotateString(s,goal))
