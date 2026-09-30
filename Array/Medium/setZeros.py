from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def setZerosBrute(self, matrix:List[List[int]])->None:
        rows = len(matrix)
        cols = len(matrix[0])
        newMat=[]
        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(-1)
            newMat.append(row)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    #down
                    for row in range(i,rows):
                        newMat[row][j] = 0
                    #up
                    for row in range(i, -1,-1):
                        newMat[row][j] = 0
                    #left
                    for col in range(j, -1,-1):
                        newMat[i][col] = 0
                    #right
                    for col in range(j, cols):
                        newMat[i][col] = 0
        
        for i in range(rows):
            for j in range(cols):
                if newMat[i][j] == 0:
                    matrix[i][j] = 0
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row=[0]*rows
        col=[0]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] ==0:
                    row[i]=1
                    col[j]=1

        for i in range(rows):
            for j in range(cols):
                if row[i] ==1 or col[j]==1:
                    matrix[i][j]=0


s= Solution()
t = int(input())

for _ in range(t):
    rows,cols = map(int, input().split())
    matrix=[]

    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    s.setZerosBrute(matrix)
    for row in matrix:
        print(*row)

