"""

https://www.interviewbit.com/problems/first-missing-integer/

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        res = [0 for i in range(len(A) + 1)]

        for i in A:
            if i > 0:
                if i < len(res):
                    res[i] = 1
        for i in range(1, len(res)):
            if res[i] == 0:
                return i
        return A[-1] + 1


print(Solution().firstMissingPositive([1, 2, 3]))



"""
Fastest Solution

def first_missing_positive(a):
    'a is unsorted, find the first missing positive integer. expect O(n) time and O(1) space.'
    for i in range(len(a)):
        v = a[i]
        while 0 < v < len(a)+1 and a[v-1] != v:
            tmp = a[v-1]
            a[v-1] = v
            v = tmp
    for i,x in enumerate(a):
        if x != i+1:
            return i+1
    return len(a)+1


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        return first_missing_positive(A)

"""