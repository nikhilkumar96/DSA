"""

https://www.interviewbit.com/problems/rotate-matrix/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]

"""


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        mat = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = A[n - j - 1][i]
        return mat


A = [
    [1, 2],
    [3, 4]
]

print(Solution().rotate(A))


"""
Fastest Solution 

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        N = len(A)
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
                A[j][N - 1 - i] = temp
        return A


"""