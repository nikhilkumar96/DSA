from header import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1 , hold2 = -math.inf, -math.inf
        release1, release2 = 0, 0  # Assume we only have 0 money at first
        for i in prices:
            release2 = max(release2, hold2+i)   # The maximum if we've just sold 2nd stock so far.
            hold2 = max(hold2, release1-i)      # The maximum if we've just buy  2nd stock so far.
            release1 = max(release1, hold1+i)   # The maximum if we've just sold 1nd stock so far.
            hold1 = max(hold1, -i)              # The maximum if we've just buy  1st stock so far.

        return release2  # Since release1 is initiated as 0, so release2 will always higher than release1

# print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
# print(Solution().maxProfit([2,4,1]))
print(Solution().maxProfit([3,2,6,5,0,3]))

# hold1 → Maximum profit after buying 1st stock
# release1 → Maximum profit after selling 1st stock
# hold2 → Maximum profit after buying 2nd stock
# release2 → Maximum profit after selling 2nd stock (final answer)