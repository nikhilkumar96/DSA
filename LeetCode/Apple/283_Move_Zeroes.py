from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        while 0 in nums:
            nums.pop(nums.index(0))
            c += 1
        nums.extend([0 for i in range(c)])

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
