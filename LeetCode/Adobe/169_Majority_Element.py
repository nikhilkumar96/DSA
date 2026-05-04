from header import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#
#         count = Counter(nums)
#         for k, v in count.items():
#             if v>len(nums)//2:
#                 return k

print(Solution().majorityElement([2,2,1,1,1,2,2]))