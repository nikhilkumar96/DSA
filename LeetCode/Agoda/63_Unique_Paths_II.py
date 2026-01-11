from header import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp= [0]*n
        dp[0]=1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]+=dp[j-1]
        return dp[-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def dfs(i, j):
            if i > m - 1 or j > n - 1 or obstacleGrid[i][j]==1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)


print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))