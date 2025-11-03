from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        for key, value in counter.items():
            heapq.heappush(res, (-value, key))

        fin = []
        for i in range(k):
            value, key = heapq.heappop(res)
            fin.append(key)
        return fin

print(Solution().topKFrequent([1,2], 2))


