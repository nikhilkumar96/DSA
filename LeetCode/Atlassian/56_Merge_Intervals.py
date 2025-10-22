from typing import List



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        res = []
        for interval in sorted_intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[4,7],[1,4]]
intervals =[[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]
# intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(Solution().merge(intervals))