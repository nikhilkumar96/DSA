from typing import List
from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # transpose
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#         # reverse vertical
#         for i in range(n):
#             for j in range(0, n//2):
#                 matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
Solution().rotate(mat)
print(mat)