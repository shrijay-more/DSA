# https://leetcode.com/problems/spiral-matrix/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def spiralOrder(self, matrix: List[List[int]])->List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left,top= 0,0
        right,bottom = cols-1, rows-1
        ans=[]
        while left <= right and top<=bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])

            for i in range(top+1,bottom+1):
                ans.append(matrix[i][right])

            if top < bottom:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[bottom][i])

            if left < right:
                for i in range(bottom-1,top,-1):
                    ans.append(matrix[i][left])

            left+=1
            top+=1
            right-=1
            bottom-=1

        return ans


s = Solution()
t = int(input())

for _ in range(t):
    rows,cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    print(s.spiralOrder(matrix))
    

    