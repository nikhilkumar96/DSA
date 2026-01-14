from header import *

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l =1
        r = max(nums)

        def get_res(div):
            sumi =0
            for num in nums:
                sumi+=math.ceil(num/div)
            return sumi

        while l<r:
            mid = int((l+r)/2)
            if get_res(mid)>threshold:
                l=mid+1
            else:
                r=mid
        return l

print(Solution().smallestDivisor([44,22,33,11,1],5))

