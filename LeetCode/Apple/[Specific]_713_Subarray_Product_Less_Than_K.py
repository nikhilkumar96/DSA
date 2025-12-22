from header import *

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k in [0, 1]:
            return 0
        count = 0
        prod = 1
        left = 0

        for right, curr in enumerate(nums):
            prod *= curr

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1  # [Specific]

        return count

print(Solution().numSubarrayProductLessThanK( nums = [10,5,2,6], k = 100))