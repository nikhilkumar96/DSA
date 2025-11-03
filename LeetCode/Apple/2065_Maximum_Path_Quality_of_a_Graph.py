from typing import List
from collections import defaultdict


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        paths = defaultdict(dict)
        for i, j, val in edges:
            paths[i][j] = val
            paths[j][i] = val

        def dfs(curr, seen,timeleft):
            res = sum([values[i] for i in seen]) if curr ==0 else 0
            for j in paths[curr].keys():
                if timeleft>=paths[curr][j]:
                    #seen | {j} means union of both set. Its equal to seen.add(j)
                    res = max(res, dfs(j, seen | {j}, timeleft-paths[curr][j]))
            return res


        return dfs(0, {0}, maxTime)

print(Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49))