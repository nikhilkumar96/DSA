from header import *
def small(matrix, m, n):
    mat =  [matrix[i][j] for i in range(m, m+3) for j in range(n, n+3) if matrix[i][j].isdigit()]
    if len(set(mat)) != len(mat):
        return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [j for j in board[i] if j.isdigit()]
            column = [board[j][i] for j in range(9) if board[j][i].isdigit()]
            if (len(set(row))!=len(row) or len(set(column))!=len(column)):
                return False
        i=0
        j=0
        while(i<9 and j<9):
            if not small(board, i, j):
                return False
            j+=3
            if j>=9:
                i+=3
                j=0
        return True



print(Solution().isValidSudoku([[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]))