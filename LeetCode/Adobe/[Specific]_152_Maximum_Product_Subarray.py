from header import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = mini = 1
        res = max(nums)
        for n in nums:
            temp = maxi*n
            maxi = max(mini*n, temp, n)
            mini = min(mini*n, temp, n)
            res = max(res, maxi)
        return res

print(Solution().maxProduct([2,3,-2,4]))