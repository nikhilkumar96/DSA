'''

https://www.interviewbit.com/problems/anti-diagonals/

Problem Description

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:

Input:

1 2 3
4 5 6
7 8 9
Return the following:
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input:
1 2
3 4
Return the following:
[
  [1],
  [2, 3],
  [4]
]

'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        m = 0
        n = len(A) - 1
        mat = [[] for i in range(len(A) * 2 - 1)]
        i, j, d = 0, 0, 0
        while i >= m and j <= n:
            p = 0
            for j in range(n + 1):
                mat[p +d].append(A[i][j])
                p += 1
            for i in range(m + 1, len(A)):
                mat[p + d].append(A[i][j])
                p += 1
            j=0
            d += 1
            i = int(d)
            m += 1
            n -= 1
        return mat


print(Solution().diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


'''
Fastest Solution

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        ans=[[] for i in range(2*len(A)-1)]
        for i in range(len(A)):
            for j in range(len(A)):
                ans[i+j].append(A[i][j])
        return ans

'''