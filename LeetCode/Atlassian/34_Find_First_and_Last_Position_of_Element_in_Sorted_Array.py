
from typing import List
def bin_search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bin_search(nums, target)
        end = bin_search(nums, target + 1) - 1
        if start <= end:
            return [start, end]
        return [-1, -1]


print(Solution().searchRange([5,7,7,8,8,10], 8))