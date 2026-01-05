from header import *


class Solution:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack_val = []
#         stack_index = []
#         ans = []
#         for i, temp in enumerate(temperatures[::-1]):
#             if stack_val:
#                 c = 0
#                 while stack_val and stack_val[0] <= temp:
#                     stack_val.pop(0)
#                     stack_index.pop(0)
#                     c += 1
#                 if stack_val:
#                     ans.append(i-stack_index[0])
#                 else:
#                     ans.append(0)
#             else:
#                 ans.append(0)
#             stack_val.insert(0, temp)
#             stack_index.insert(0, i)
#         return ans[::-1]

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))