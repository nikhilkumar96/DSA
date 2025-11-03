from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        localmin = prices[0]

        for price in prices[1:]:
            if price <=localmin:
                localmin =price
            elif price > localmin:
                maxprof+=price-localmin
                localmin = price
        return maxprof


print(Solution().maxProfit([7,1,5,3,6,4]))