# https://leetcode.com/problems/merge-intervals/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ans.append(intervals[0])
        for i in range(1,n):
            row = intervals[i]
            if row[0] <= ans[len(ans)-1][1]:
                ans[len(ans)-1][1] = max(row[1],  ans[len(ans)-1][1])
            else:
                ans.append(row)
        
        return ans


s = Solution()
t = int(input())

for _ in range(t):
    rows = int(input())
    intervals =[]
    for i in range(rows):
        row = list(map(int, input().split()))
        intervals.append(row)
    print(s.merge(intervals))
        