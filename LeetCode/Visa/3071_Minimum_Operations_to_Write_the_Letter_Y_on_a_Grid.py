from header import *
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y = [0,0,0]
        x = [0,0,0]

        for i in range(n):
            for j in range(n):
                if (i<n//2 and (i==j or i==n-1-j)) or (i>=n//2 and j==n//2):
                    y[grid[i][j]]+=1
                else:
                    x[grid[i][j]]+=1
        temp = []
        for i in range(3):
            for j in range(3):
                if i!=j:
                    temp.append(sum(y)-y[i]+sum(x)-x[j])
        return min(temp)


print(Solution().minimumOperationsToWriteY([[0,0,1],[0,0,2],[1,0,2]]))