# https://leetcode.com/problems/sudoku-solver/description/
class Solution:
    def isPossible(self, board, row, col, ch):
        startRow = 3 * (row // 3)
        startCol = 3 * (col // 3)

        # Check 3x3 box
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == ch:
                    return False

        # Check row and column
        for i in range(9):
            if board[row][i] == ch:
                return False
            if board[i][col] == ch:
                return False

        return True

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for ch in range(1, 10):
                        ch = str(ch)

                        if self.isPossible(board, i, j, ch):
                            board[i][j] = ch

                            if self.solve(board):
                                return True

                            board[i][j] = '.'

                    return False

        return True

    def solveSudoku(self, board):
        self.solve(board)

sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(board)
print(board)