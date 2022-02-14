"""

https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1].

Note: Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        arr = [[1], [1, 1], [1, 2, 1]]
        if A < 3:
            return arr[A]
        else:
            for i in range(2, A):
                temp = arr[-1]
                res = [1]
                for j in range(1, len(temp)):
                    res.append(temp[j] + temp[j - 1])
                res.append(1)
                arr.append(res)
            return arr[-1]


print(Solution().getRow(4))

"""
Fastest Solution


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, a):
        ans, n = [], 1
        for i in range(a + 1):
            ans.append(n)

            n *= (a - i)
            n //= (i + 1)
        return ans

"""
