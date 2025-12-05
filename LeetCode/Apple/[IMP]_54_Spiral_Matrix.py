from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]  # [IMP]  #transpose matrix = list(zip(*matrix))
        return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(Solution().spiralOrder(matrix))

