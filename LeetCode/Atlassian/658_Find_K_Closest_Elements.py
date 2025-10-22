from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = l + (r - l) // 2
            if arr[m + k] <= x:
                l = m + 1
            else:
                middist = abs(x - arr[m])
                midkdist = abs(x - arr[m + k])

                if middist <= midkdist:
                    r = m
                else:
                    l = m + 1

        return arr[l:l + k]


# def findclose(arr, i, j, x):
#     if  i is None:
#         return j
#     if j is None:
#         return i
#     if abs(arr[i] - x) == abs(x - arr[j]) or abs(arr[i] - x) < abs(x - arr[j]):
#         return i
#     else:
#         return j
#
#
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         closest = None
#         if x in arr:
#             closest = arr.index(x)
#         else:
#             if x < arr[0]:
#                 closest = 0
#             elif x > arr[-1]:
#                 closest = len(arr) - 1
#             else:
#                 for i in range(1, len(arr)):
#                     if x > arr[i - 1] and x < arr[i]:
#                         closest = findclose(arr, i-1, i, x)
#
#         res = [arr[closest]]
#         back = closest - 1 if closest - 1 >= 0 else None
#         forth = closest + 1 if closest + 1 <= len(arr) - 1 else None
#
#         while len(res) != k:
#             next_close = findclose(arr, back, forth, x)
#             if next_close == back:
#                 res.insert(0, arr[next_close])
#                 back = back-1 if back-1 >= 0 else None
#             else:
#                 res.append(arr[next_close])
#                 forth = forth + 1 if forth + 1 <= len(arr) - 1 else None
#
#         return res



obj = Solution()
print(obj.findClosestElements([1,2,3,4,5],4, 3))


