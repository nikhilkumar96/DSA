from header import *
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()

        def dfs(i, j, curr):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != curr or (i, j) in seen:
                return False

            image[i][j] = color
            seen.add((i, j))

            dfs(i - 1, j, curr)
            dfs(i + 1, j, curr)
            dfs(i, j - 1, curr)
            dfs(i, j + 1, curr)

            return True

        dfs(sr, sc, image[sr][sc])
        return image

print(Solution().floodFill( image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))