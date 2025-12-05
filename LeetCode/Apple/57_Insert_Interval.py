from header import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for l, r in sorted(intervals+[newInterval]):
            if res and res[-1][1]>=l:
                res[-1][1] = max(res[-1][1], r)
            else:
                res.append([l,r])
        return res



# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         i =0
#         while i<len(intervals) and intervals[i][0]<newInterval[0]:
#             i+=1
#         intervals.insert(i, newInterval)
#
#         j=1
#         while j<len(intervals):
#             if intervals[j][0]<=intervals[j-1][1]:
#                 left = intervals.pop(j-1)
#                 right = intervals.pop(j-1)
#                 intervals.insert(j-1, [left[0], max(left[1], right[1])])
#             else:
#                 j+=1
#         return intervals

print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))