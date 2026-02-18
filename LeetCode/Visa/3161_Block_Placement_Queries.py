from header import *

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obs = []
        dp = []
        res = []

        def add_obstacle(obstacle_list, dp_list, obstacle, re_calc=True):
            i = bisect_right(obstacle_list, obstacle)
            obstacle_list.insert(i, obstacle)
            if i == 0:
                dp_list.insert(i, obstacle)
            else:
                dp_list.insert(i, max([dp_list[i - 1], obstacle - obstacle_list[i - 1]]))
            if re_calc:
                for j in range(i + 1, len(obstacle_list)):
                    dp_list[j] = max([dp_list[j - 1], obstacle_list[j] - obstacle_list[j - 1]])
            return i

        for q in queries:
            if q[0] == 1:
                add_obstacle(obs, dp, q[1])
            else:
                if q[2] > q[1]:
                    res.append(False)
                elif not obs:
                    res.append(True)
                else:
                    temp_obstacle, temp_dp = deepcopy(obs), deepcopy(dp)
                    i = add_obstacle(temp_obstacle, temp_dp, q[1],False)
                    if temp_dp[i]>=q[2]:
                        res.append(True)
                    else:
                        res.append(False)
        return res


print(Solution().getResults([[1,2],[1,3],[2,3,6],[2,5,5],[2,9,5]]))




