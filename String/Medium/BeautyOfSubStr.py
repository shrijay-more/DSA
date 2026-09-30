# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0]*26
            for j in range(i,n):
                freq[ord(s[j]) - ord('a')]+=1
                maxi = max(freq)
                mini = min([f for f in freq if f > 0])
                if mini != 0:
                    ans+=(maxi-mini)

        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    s= str(input())
    sol.beautySum(s)