from header import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         maxheap = []
#         for i in nums:
#             heapq.heappush(maxheap, -i)
#         for i in range(k-1):
#             heapq.heappop(maxheap)
#         return -maxheap[0]

print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))