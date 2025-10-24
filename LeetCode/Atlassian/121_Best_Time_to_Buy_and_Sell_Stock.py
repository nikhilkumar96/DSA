from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = math.inf
        total_max=0
        if len(prices)==2 and prices[0]<prices[1]:
            return prices[1]-prices[0]
        for i in range(len(prices)):
            if prices[i]<current_min:
                current_min = prices[i]
            elif prices[i]-current_min>total_max:
                total_max=prices[i]-current_min

        return total_max

obj = Solution()
a = [1,2,4]
print(obj.maxProfit(a))