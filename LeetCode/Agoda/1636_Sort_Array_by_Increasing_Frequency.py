from header import *

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        di = SortedDict()
        for k, v in Counter(nums).items():
            if v not in di:
                di[v] = [k]
            else:
                di[v].append(k)
        res = []
        for k, v in di.items():
            temp = sorted(v, reverse=True)
            for val in temp:
                res+=[val]*k
        return res

print(Solution().frequencySort([1,1,2,2,2,3]))