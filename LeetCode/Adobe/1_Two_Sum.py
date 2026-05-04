from header import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:] and nums.index(target-nums[i])!=i:
                return [i, nums.index(target-nums[i])]



print(Solution().twoSum( nums = [2,7,11,15], target = 9))