'''

https://www.interviewbit.com/problems/hotel-bookings-possible/


Problem Description

A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain
an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the
demand. Write a program that solves this problem in time O(N log N) .



Input Format
First argument is an integer array A containing arrival time of booking.

Second argument is an integer array B containing departure time of booking.

Third argument is an integer C denoting the count of rooms.



Output Format
Return True if there are enough rooms for N bookings else return False.

Return 0/1 for C programs.



Example Input
Input 1:

 A = [1, 3, 5]
 B = [2, 6, 8]
 C = 1


Example Output
Output 1:

 0


Example Explanation
Explanation 1:

 At day = 5, there are 2 guests in the hotel. But I have only one room
'''


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        di = {}

        for i in range(len(arrive)):
            di[arrive[i]] = depart[i]

        di = dict(sorted(di.items(), key=lambda item: item[0]))
        prev = None
        last_k = []
        for k, v in di.items():
            for item in last_k:
                if item < k:
                    K += 1
                    last_k.remove(item)
            if prev is None:
                prev = v
            elif prev > k:
                K -= 1
                last_k.append(max(prev, v))
                if K < 1:
                    return 0
            prev = max(prev, v)
        return 1


A = [47, 4, 0, 12, 47, 31, 15, 49, 29, 33, 7, 22, 26, 24, 16]
B = [95, 4, 26, 16, 51, 79, 43, 58, 32, 80, 30, 27, 29, 54, 16]
C = 10

print(Solution().hotel(A, B, C))

'''
Fastest Solution

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()

        for i in range(len(arrive) - K):
            if depart[i] > arrive[i + K]:
                return False
        else:
            return True

'''
