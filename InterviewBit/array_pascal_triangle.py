"""

https://www.interviewbit.com/problems/pascal-triangle/

Given numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
Constraints:
0 <= numRows <= 25

"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return []

        arr = [[1]]

        for i in range(1, A):
            res = [1]
            for j in range(1, len(arr[-1])):
                res.append(arr[-1][j] + arr[-1][j - 1])
            res.append(1)
            arr.append(res)
        return arr


print(Solution().solve(3))

"""

Fastest Solution

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        a=[]
        for i in range(A):
            a.append([1]*(i+1))
            #print(a)
        for i in range(2,A):
            for j in range(1,i):
                a[i][j]=a[i-1][j-1]+a[i-1][j]
        #print(a)
        return a

"""
