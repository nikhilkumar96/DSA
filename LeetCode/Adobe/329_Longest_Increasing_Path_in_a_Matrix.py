from header import *

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [ [-1]*n for _ in range(m)]
        res =0
        def dfs(i, j, prev):
            if i<0 or j<0 or i>=m or j>=n or prev>=matrix[i][j]:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]

            up = dfs(i-1, j, matrix[i][j])
            down = dfs(i+1, j, matrix[i][j])
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])
            memo[i][j] = max(up, down, left, right)+1
            return memo[i][j]

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j, -1))
        return res



# print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[1,2]]))