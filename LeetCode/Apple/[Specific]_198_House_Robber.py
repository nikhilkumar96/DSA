from header import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)   # [Specific]
        return now

print(Solution().rob([2,1,1,2]))