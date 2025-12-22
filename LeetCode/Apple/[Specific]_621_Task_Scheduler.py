import heapq

from header import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())
        num_max = sum([1 for i in count.values() if i == max_freq])

        # Formula - (max_freq − 1) × (n + 1) + num_max                          [Specific]
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         count = Counter(tasks)
#         heap = []
#         limit = {}
#         for k, v in count.items():
#             heapq.heappush(heap, (-v, k))
#             limit[k] = -1
#
#         t = 0
#         res = 0
#
#         while tasks:
#             temp = []
#             while heap:
#                 v, k = heapq.heappop(heap)
#                 v=-v
#                 if limit[k] < t:
#                     v-=1
#                     if v>0:
#                         temp.append([v,k])
#                     limit[k] = t + n
#                     tasks.remove(k)
#                     break
#                 if v>0:
#                     temp.append([v,k])
#
#             for v, k in temp:
#                 heapq.heappush(heap, (-v, k))
#             t += 1
#             res += 1
#         return res

print(Solution().leastInterval(tasks = ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n = 7))

