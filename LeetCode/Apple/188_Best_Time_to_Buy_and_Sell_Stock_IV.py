from header import *
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        hold = [-math.inf for _ in range(k)]
        release = [0 for _ in range(k)]

        for i in prices:
            for j in range(k-1, -1, -1):
                release[j] = max(release[j], hold[j]+i)
                if j-1>=0:
                    hold[j] = max(hold[j], release[j-1]-i)
                else:
                    hold[j] = max(hold[j], -i)
        return release[-1]


print(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]))