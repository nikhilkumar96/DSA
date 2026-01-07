from header import *

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        pair = []

        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i - 1]
            if curr_diff < min_diff:
                min_diff = curr_diff
                pair = [[arr[i - 1], arr[i]]]
            elif curr_diff == min_diff:
                pair.append([arr[i - 1], arr[i]])
        return pair

print(Solution().minimumAbsDifference([4,2,1,3]))
