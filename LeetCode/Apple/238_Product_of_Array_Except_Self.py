import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        return [int(prod/nums[i]) if nums[i] else math.prod(nums[:i]+nums[i+1:]) for i in range(len(nums))]

print(Solution().productExceptSelf([-1,1,0,-3,3]))