from header import *

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = float('-inf')
        release = 0

        for price in prices:
            release = max(release, hold + price - fee)
            hold = max(hold, release - price)

        return release

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#
#         def maxProfit_with_k(k: int) -> int:
#             hold = [-math.inf for _ in range(k)]
#             release = [0 for _ in range(k)]
#
#             for i in prices:
#                 for j in range(k-1, -1, -1):
#                     release[j] = max(release[j], hold[j]+i)
#                     if j-1>=0:
#                         hold[j] = max(hold[j], release[j-1]-i)
#                     else:
#                         hold[j] = max(hold[j], -i)
#             return release[-1]
#
#         l=1
#         r=len(prices)//2
#         while l<r:
#             m= (l+r)//2
#             k_buy = maxProfit_with_k(m) - (fee*m)
#             k_buy2 = maxProfit_with_k(m+1) - (fee* (m+1))
#             if k_buy<k_buy2:
#                 l=m+1
#             else:
#                 r=m
#         return max(0, maxProfit_with_k(l) - (fee*l))

print(Solution().maxProfit(prices = [1,3,2,8,4,9], fee = 2))