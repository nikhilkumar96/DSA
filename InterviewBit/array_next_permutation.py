'''

https://www.interviewbit.com/problems/next-permutation/

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

Note:

1. The replacement must be in-place, do **not** allocate extra memory.
2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
Input Format:

The first and the only argument of input has an array of integers, A.
Output Format:

Return an array of integers, representing the next permutation of the given array.
Constraints:

1 <= N <= 5e5
1 <= A[i] <= 1e9
Examples:

Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]

'''


import math


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        c = -1
        res = sorted(A)

        if A == res[::-1]:
            return res
        elif A == res:
            temp = res[-1]
            res[-1] = res[-2]
            res[-2] = temp
            return res
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                c = i
        if c+1 == len(A):
            temp = A[-3]
            A.pop(-3)
            return A +[temp]
        mini = math.inf
        mini_i = -1
        for i in range(c + 1, len(A)):
            if A[i] > A[c + 1] and A[i] < mini:
                mini = A[i]
                mini_i = i
        A.pop(mini_i)
        return A[:c + 1] + [mini] + A[c + 1:]


print(Solution().nextPermutation(
    [1,2,3]))


'''
Fastest and Correct Solution


    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, a):
        
        i = len(a) - 2
        while not (i < 0 or a[i] < a[i+1]):
            i -= 1
        if i < 0:
            sorting = sorted(a)
            return sorting
        j = len(a) - 1
        while not (a[j] > a[i]):
            j -= 1
        a[i], a[j] = a[j], a[i]        
        a[i+1:] = reversed(a[i+1:])  
        return a

'''
