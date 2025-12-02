from header import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_num1 = set()
        set_num2 = set()
        for i in nums:
            if i not in set_num1:
                set_num1.add(i)
            else:
                set_num2.add(i)
        return next(iter(set_num1 - set_num2))
