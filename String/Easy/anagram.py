# https://leetcode.com/problems/valid-anagram/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')]+=1
            freq[ord(t[i]) - ord('a')]-=1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False

        return True

sol = Solution()
t = int(input())

for _ in range(t):
    s,t = map(str, input().split())
    sol.isAnagram(s,t)
