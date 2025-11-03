from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        a = len(nums) - k
        temp = nums[:a]
        nums[:a] = []
        nums.extend(temp)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             nums.insert(0, nums.pop(-1))


nums = [1,2,3,4,5,6,7]
k =3

Solution().rotate(nums, k)
print(nums)