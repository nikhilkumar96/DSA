from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_ele = Counter(nums)
        return [key for key, value in count_ele.items() if value>len(nums)//3]


print(Solution().majorityElement([3,2,3]))