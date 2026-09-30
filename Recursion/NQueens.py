from typing import List

def isSafe(mat: List[List[str]], row: int, col: int) -> bool:
    delRow = [1, 1, 1]
    delCol = [0, 1, -1]

    for i in range(3):
        newRow = row - delRow[i]
        newCol = col - delCol[i]

        while newRow >= 0 and newCol >= 0 and newCol < len(mat):
            if mat[newRow][newCol] == 'Q':
                    return False

            newRow = newRow - delRow[i]
            newCol = newCol - delCol[i]

    return True

def solveNQueensHelper(mat: List[List[str]],n: int,row: int,ans: List[List[str]]) -> None:
    if row == n:
        temp = []

        for i in range(n):
            s = ""
            for j in range(n):
                s += mat[i][j]
            temp.append(s)

        ans.append(temp)
        return

    for col in range(n):
        if mat[row][col] == '.' and isSafe(mat, row, col):
            mat[row][col] = 'Q'
            solveNQueensHelper(mat, n, row + 1, ans)
            mat[row][col] = '.'

def solveNQueens(n: int) -> List[List[str]]:
    mat = [['.'] * n for _ in range(n)]
    ans = []
    solveNQueensHelper(mat, n, 0, ans)
    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    ans = solveNQueens(n)
    print(ans)