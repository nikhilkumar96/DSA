from header import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)+1)//2) - sum(nums)

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         return next(iter(set([i for i in range(len(nums)+1)]).difference(nums))) #[IMP]

print(Solution().missingNumber([1,3,0]))