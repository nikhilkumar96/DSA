"""
https://www.interviewbit.com/problems/word-ladder-i/

Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.
Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3
Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"


"""

import math
import sys
sys.setrecursionlimit(100000)


class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer

    def check_distance(self, a, b):
        return sum([a[i] != b[i] for i in range(len(a))])

    def recur(self, A, B, C, res, count):
        if self.check_distance(A, B) == 1:
            return count + 1
        else:
            maxi = math.inf
            for item in C:
                if self.check_distance(item, A) == 1 and item not in res:
                    if item == B:
                        maxi = min(maxi, count)
                    else:
                        maxi = min(maxi, self.recur(item, B, C, res + [item], count + 1))
            return maxi

    def solve(self, A, B, C):
        return self.recur(A, B, C, [], 0) + 1





A = "sgtra"
B = "plvgf"
C = ["pjvgf", "pgtra", "pglga", "pgwra", "pgggf", "pglra", "ppggf", "ppvgf", "pggga", "sgtra", "plvgf"]

print(Solution().solve(A, B, C))



"""

Editorial Solution

import collections


class Solution:
    # @param begin : string
    # @param end : string
    # @param words : list of strings
    # @return an integer
    def solve(self, begin, end, words):
        if not begin in words or not begin or not end or not words:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(begin)):
            for word in words:
                graph[word[:i] + '?' + word[i + 1:]].append(word)

        queue = collections.deque([(begin, 1)])
        visited = {begin}
        while queue:
            current, level = queue.popleft()
            for i in range(len(current)):
                intermediate = current[:i] + '?' + current[i + 1:]
                for word in graph[intermediate]:
                    if word == end:
                        return level + 1
                    if not word in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                del graph[intermediate]
        return 0

"""