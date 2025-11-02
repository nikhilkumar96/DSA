from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, currsum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= currsum and currsum < 0:
                currsum = nums[i]
            else:
                currsum += nums[i]

            maxsum = max(maxsum, currsum)
        return maxsum


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))