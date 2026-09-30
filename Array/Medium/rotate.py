# https://leetcode.com/problems/rotate-image/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            row[:] = row[::-1]         

s =Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    matrix=[]
    for i in range(n):
        for j in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
    
    s.rotate(matrix)
    for row in matrix:
        print(*row)