from header import *

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        res = {}

        for w in wall:
            curr_sum=0
            for j in w[:-1]:
                curr_sum+=j
                if curr_sum in res:
                    res[curr_sum]+=1
                else:
                    res[curr_sum]=1
        return len(wall)-max(res.values()) if res else len(wall)


# print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
print(Solution().leastBricks([[1],[1],[1]]))
# print(Solution().leastBricks([[1,1],[2],[1,1]]))