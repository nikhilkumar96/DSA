from header import *
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j])
        c=0
        while q:
            temp = []
            rot = False
            for i, j in q:
                if i+1<m and grid[i+1][j]==1:
                    grid[i + 1][j] =2
                    temp.append([i+1,j])
                    rot = True
                if j+1<n and grid[i][j+1]==1:
                    grid[i][j+1] = 2
                    temp.append([i,j+1])
                    rot = True
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j] = 2
                    temp.append([i-1,j])
                    rot = True
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1] = 2
                    temp.append([i,j-1])
                    rot = True
            q = temp
            if rot:
                c+=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return c



print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))