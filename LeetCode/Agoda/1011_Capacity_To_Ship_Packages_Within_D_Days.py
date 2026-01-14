from header import *

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumi = sum(weights)
        block = math.ceil(sumi / days)
        l = block if block>max(weights) else max(weights)
        r = sum(weights)

        while l <r:
            mid = int((l+r)/2)
            c=1
            curr_sum =0
            for w in weights:
                if curr_sum+w>mid:
                    c+=1
                    curr_sum=0
                curr_sum+=w
            if c>days:
                l = mid+1
            else:
                r = mid
        return l

print(Solution().shipWithinDays(weights = [147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47],
                                days = 10))