"""

https://www.interviewbit.com/problems/spiral-order-matrix-ii/

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000
Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]

"""


def generateMatrix(A):
    l = 0
    r = A - 1
    u = 0
    d = A - 1
    i = 0
    j = 0
    flag = 'right'
    mat = [[0 for p in range(A)] for q in range(A)]
    n = 1
    while n <= A ** 2:
        mat[i][j] = n
        print(mat)
        n += 1
        if flag == 'right':
            if j < r:
                j += 1
            else:
                u += 1
                i += 1
                flag = 'down'
        elif flag == 'down':
            if i < d:
                i += 1
            else:
                r -= 1
                j -= 1
                flag = 'left'
        elif flag == 'left':
            if j > l:
                j -= 1
            else:
                d -= 1
                i -= 1
                flag = 'up'
        else:
            if i > u:
                i -= 1
            else:
                l += 1
                j += 1
                flag = 'right'
    return mat


a = generateMatrix(80)
print(a)

"""
Fastest Solution


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        l,r,t,b=0,A-1,0,A-1
        ans=[[0]*A for _ in range(A)] 
        num=1
        while(l<=r and t<=b):
            for i in range(l,r+1):
                ans[t][i] = num
                num+=1
            t+=1
            for i in range(t,b+1):
                ans[i][r]= num
                num+=1
            r-=1
            for i in range(r,l-1,-1):
                ans[b][i] = num 
                num+=1
            b-=1
            for i in range(b,t-1,-1):
                ans[i][l] = num
                num+=1
            l+=1
        return ans
"""
