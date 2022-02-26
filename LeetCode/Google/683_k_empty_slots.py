"""

https://leetcode.com/problems/k-empty-slots/

You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb
every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at
position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs
between them that are all turned off. If there isn't such day, return -1.


Example 1:

Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: bulbs = [1,2,3], k = 1
Output: -1


"""


class Solution:

    def checkCondition(self, res, k):
        maxi = 0
        flag = False
        c = 0
        for i in res:
            if i:
                if flag:
                    if c == k:
                        return True
                    maxi = max(maxi, c)
                    c = 0
                elif c:
                    maxi = max(maxi, c - 1)
                    flag = True
                    c = 0
                else:
                    flag = True
            else:
                c += 1
        maxi = max(maxi, c)
        if maxi < k:
            return -1
        return False

    def dayPass(self, bulb, k, i, res):
        res[bulb[i] - 1] = True
        temp = self.checkCondition(res, k)
        if i + 1 == len(bulb) or temp == -1:
            return -1
        elif temp:
            return i + 1
        else:
            return self.dayPass(bulb, k, i + 1, res)

    def kEmptySlots(self, bulbs, k: int) -> int:
        return self.dayPass(bulbs, k, 0, [False for i in bulbs])


print(Solution().kEmptySlots([6, 10, 7, 1, 9, 8, 4, 3, 5, 2], 3))

"""
Better Solution

import bisect
class Solution(object):
    def kEmptySlots(self, bulbs, K):

        timePassed = []
        for i, bulb in enumerate(bulbs):
            # Where do we insert today's bulb?
            insertLoc = bisect.bisect_left(timePassed, bulb)
            timePassed.insert(insertLoc, bulb)
            v1, v2 = 0, 0
            # Location of our neighboring bulbs
            prevLoc, nextLoc = insertLoc - 1, insertLoc + 1
            # Check if either neighbor is K apart from the bulb turned on today
            if prevLoc >= 0:
                if abs(timePassed[prevLoc] - timePassed[insertLoc]) == K + 1:
                    v1 = max(bulbs[timePassed[prevLoc]-1], bulbs[timePassed[insertLoc]-1])
            if nextLoc < len(timePassed):
                if abs(timePassed[insertionPoint] - timePassed[nextLoc]) == K + 1:
                    v2 = max(bulbs[timePassed[insertLoc]-1], bulbs[timePassed[nextLoc]-1])
            if v1 or v2:
                return len(timePassed)

        return -1

"""
