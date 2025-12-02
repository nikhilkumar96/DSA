from header import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if not nums:
            return 0
        curr = nums[0]
        curr_len = 1
        max_len = 1
        for i  in nums[1:]:
            if curr == i:
                continue
            if curr+1 == i:
                curr_len+=1
            else:
                curr_len=1
            curr =i
            if max_len<curr_len:
                max_len = curr_len
        return max_len

print(Solution().longestConsecutive([100,4,200,1,3,2]))