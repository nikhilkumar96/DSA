from header import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))  # [IMP]


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def back_track(i):
#             if i == len(nums):
#                 res.append(nums[:])  # need to create shallow copy of the array.. it is equal to  temp = copy(nums);res.append(temp)
#                 return
#             for j in range(i, len(nums)):
#                 nums[i], nums[j] = nums[j], nums[i]
#                 back_track(i+1)
#                 nums[i], nums[j] = nums[j], nums[i]  #switching to original order
#         back_track(0)
#         return res

print(Solution().permute([1,2,3]))