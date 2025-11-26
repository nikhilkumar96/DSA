from typing import List
import heapq

def pop_neg(nums):
    while nums and nums[0] <=0:
        heapq.heappop(nums)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        flag = False
        if min(nums)<=0:
            flag = True
        heapq.heapify(nums)
        if flag:
            pop_neg(nums)
        if nums:
            old = heapq.heappop(nums)
            if old != 1:
                return 1
        else:
            return 1
        while nums:
            curr = heapq.heappop(nums)
            if curr == old+1 or curr == old:
                old = curr
                continue
            return old+1
        return old+1





print(Solution().firstMissingPositive([0,-1,3,1]))