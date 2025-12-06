from header import *

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        temp = SortedList(nums[0:k])
        flag = False
        res = []
        half = k // 2
        if k % 2 == 0:
            flag = True
        if flag:
            res.append(float((temp[half] + temp[half - 1]) / 2))
        else:
            res.append(float(temp[half]))

        for i in range(0, len(nums) - k):
            temp.remove(nums[i])
            temp.add(nums[i + k])
            if flag:
                res.append(float((temp[half] + temp[half - 1]) / 2))
            else:
                res.append(float(temp[half]))
        return res

#
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         res = []
#         for i in range(len(nums)-k+1):
#             res.append(float(statistics.median(nums[i:i+k])))   # [IMP]
#         return res

print(Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))