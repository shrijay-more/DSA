# https://leetcode.com/problems/pascals-triangle/
from typing import List
import sys

sys.stdin = open('z.txt','r')

# formula to get the row and col
# row-1 / col-1 * (row-col)
class Solution:
    def generate(self, rows:int)->List[List[int]]:
        if rows == 0 :
            return
        dp = []

        for i in range(rows):
            row = [1] * (i+1)

            for j in range(1,i):
                row[j] = dp[i-1][j-1] + dp[i-1][j] 

            dp.append(row)

        return dp


    
s = Solution()
t = int(input())

for _ in range(t):
    row = int(input())
    print(s.generate(row))