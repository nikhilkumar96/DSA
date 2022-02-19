"""

https://www.interviewbit.com/problems/find-duplicate-in-array/

Problem Description

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
Sample Input:

[3 4 1 4 1]

Sample Output:

1

If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1

"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        my_set = set()
        for i in A:
            old_len = len(my_set)
            my_set.add(i)
            if len(my_set) == old_len:
                return i
        return -1


print(Solution().repeatedNumber([1, 4, 4, 1, 3]))

"""
Fastest Solution

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        sumOfList = sum(A)
        n = len(A)
        sumOfRange = int(n * (n + 1) / 2) - n
        return sumOfList - sumOfRange

"""
