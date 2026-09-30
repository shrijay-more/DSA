# https://leetcode.com/problems/longest-palindromic-substring/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def longestPalindromeBrute(self, s: str) -> str:
        n = len(s)
        ans= ""
        for i in range(n):
            temp=""
            for j in range(i,n):
                temp+=s[j]
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans=temp
        return ans
    
    def expand(self,s:str, l:int, r:int) ->str:
        while l>=0  and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        # pallindromic substring expand from middle 
        # main intuition
        n = len(s)
        ans=""
        for i in range(n):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)
            ans = max(ans,odd,even,key=len)
        
        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    sol.longestPallindromeBrute(s)
