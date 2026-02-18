from header import *

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = [dist[i]/speed[i] for i in range(len(dist))]
        arrival.sort()
        for i in range(len(arrival)):
            if arrival[i]<=i:
                return i
        return len(dist)

# class Solution:
#     def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         arrival = []
#         def monster_to_kill():
#             if not arrival:
#                 for i in range(len(dist)):
#                     arrival.append(dist[i]/speed[i])
#             return arrival.index(min(arrival))
#
#         def kill(idx):
#             if 0 in dist:
#                 return False
#             dist.pop(idx)
#             speed.pop(idx)
#             arrival.pop(idx)
#             return True
#
#         def update_dist():
#             for i in range(len(dist)):
#                 dist[i]-=speed[i]
#                 if dist[i]<1:
#                     return False
#             return True
#
#         c = 0
#         while dist:
#             if not kill(monster_to_kill()):
#                 break
#             else:
#                 c += 1
#                 if not update_dist():
#                     break
#         return c

print(Solution().eliminateMaximum([1,1,2,3], [1,1,1,1]))