from header import *
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False

        count = Counter(nums)

        for v in count.values():
            if v>2:
                return False
        return True

print(Solution().isPossibleToSplit([1,1,2,2,3,4]))