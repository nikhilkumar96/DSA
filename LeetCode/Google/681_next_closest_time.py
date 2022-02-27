"""

https://leetcode.com/problems/next-closest-time/

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are
all invalid.



Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

"""


class Solution:
    def checkvalid(self, time):
        if int("".join(time[:2])) < 24 and int("".join(time[2:])) < 60:
            return True
        return False

    def getbigger(self, res, num, limit):
        for i in res:
            if i > num and i <= limit:
                return i
        return -1

    def getsmaller(self, res, limit, num=None):
        for i in res:
            if num and i > num and i <= limit:
                return i
            if not num and i <= limit:
                return i
        return - 1

    def nextClosestTime(self, time: str) -> str:
        di = {
            0: 2,
            1: 9,
            2: 5,
            3: 9
        }
        res = []
        for i in time:
            if i != ':':
                res.append(int(i))
        time, prev_time = list(res), list(res)
        res.sort()
        temp_flag = False
        flag = False
        i = 3
        while i < 4 and i >= 0:
            if not flag and not temp_flag:
                temp = self.getbigger(res, time[i], di[i])
                if temp == -1:
                    i -= 1
                    if i == -1:
                        temp_flag = True
                        i += 1
                else:
                    time[i] = temp
                    flag = True
                    i += 1
            else:
                if temp_flag:
                    temp = self.getsmaller(res, di[i], time[i])
                    if temp != -1:
                        time[i] = temp
                        temp_flag = False
                        flag = True
                else:
                    temp = self.getsmaller(res, di[i])
                    if temp != -1:
                        time[i] = temp
                i += 1

        same = True if time == prev_time else False

        time = [str(i) for i in time]
        if not self.checkvalid(time) or same:
            temp = min(res)
            return f"{temp}{temp}:{temp}{temp}"
        return ''.join(time[:2]) + ":" + ''.join(time[2:])


print(Solution().nextClosestTime("15:55"))

"""
Fastest Solution

from itertools import product as iterprod

class Solution:
    def nextClosestTime(self, time: str) -> str:
        hrs, mins = map(int, time.split(':'))
        self.nums = set(time.replace(':', ''))
        maxmins = self.maxmins(mins, 60)
        if int(maxmins) > mins:
            equals = True
        else:
            equals = False
        maxhrs = self.maxmins(hrs, 24, equals=equals)
        return f'{maxhrs:02}:{maxmins:02}'

        
    def maxmins(self, val, limit, equals=False):
        if equals:
            new = [int(''.join(x)) for x in iterprod(self.nums, self.nums) if val <= int(''.join(x)) < limit]
        else:
            new = [int(''.join(x)) for x in iterprod(self.nums, self.nums) if val < int(''.join(x)) < limit]
        return min(new) if new else int(min(self.nums)*2)
"""
