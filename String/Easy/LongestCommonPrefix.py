# http://leetcode.com/problems/longest-common-prefix/
from typing import List
import sys

sys.stdin = open('z.txt','r')
class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        first_ele = strs[0]
        for i in range(len(first_ele)):
            for j in range(1, n):
                if i >= len(strs[j]) or first_ele[i] != strs[j][i]:
                    return first_ele[:i]
        return first_ele



sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    sol.longestCommonPrefix(arr)
