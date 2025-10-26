from typing import List

def dfs(mat, i, j, row, col, cells):
    if i == 0 and j == 0:
        for coord in cells:
            mat[coord[0]-1][coord[1]-1] = 1
    elif i == row - 1 and mat[i][j] == 0:
        return True
    if mat[i][j] != 0:
        return False

    mat[i][j] = 2

    top, left, bottom, right = False, False, False, False

    if i - 1 >= 0:
        top = dfs(mat, i - 1, j, row, col, cells)
    if j - 1 >= 0:
        left = dfs(mat, i, j - 1, row, col, cells)
    if i + 1 < row:
        bottom = dfs(mat, i + 1, j, row, col, cells)
    if j + 1 < col:
        right = dfs(mat, i, j + 1, row, col, cells)
    return top or left or bottom or right

def cancross(mat, row, col, cells):
    for i in range(col):
        if dfs(mat, 0, i, row, col, cells):
            return True
    return False

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left = 1
        right = len(cells)
        while left < right:
            mat = [[0 for i in range(col)] for i in range(row)]

            mid = right - (right -left) // 2

            res = cancross(mat, row, col, cells[:mid])
            if res:
                left = mid
            else:
                right = mid-1
        return left

print(Solution().latestDayToCross(2,2, [[1,1],[1,2],[2,1],[2,2]]))
print(Solution().latestDayToCross(2,2, [[1,1],[2,1],[1,2],[2,2]]))