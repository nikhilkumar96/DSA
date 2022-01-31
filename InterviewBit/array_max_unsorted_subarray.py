"""

https://www.interviewbit.com/problems/maximum-unsorted-subarray/

You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.

Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.

If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.

"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        arr = list(range(len(A)))
        arr.sort(key=lambda x: A[x])
        res = [-1]
        flag = False

        for i in range(len(A)):
            if i != arr[i]:
                if flag:
                    if len(res) < 2:
                        res.append(i)
                    else:
                        res[1] = i
                else:
                    res[0] = i
                    flag = True
        return res


print(Solution().subUnsort([3, 3, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 15, 20, 16]))

"""
Fastest Solution

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        A_sorted = sorted(A) 
        #print(A_sorted)

        start,end=-1,-1
        for i in range(n):
            A[i] = A[i] - A_sorted[i]
        #print(A)
        for i in range(n-1):
            if(A[0]!=0):
                start=0
                break
            if(A[i]==0 and A[i+1]!=0):
                start = i+1
                break
        #print(start)
        for i in range(n-1,0,-1):
            if(A[n-1]!=0):
                end = n-1
                break
            if(A[i]==0 and A[i-1]!=0):
                end = i-1
                break
        #print(end)
        if(start==-1 and end==-1):
            return [-1]
        return [start, end]
"""
