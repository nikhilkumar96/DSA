from  header import *


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        count = [0] * k
        server = []

        for i in range(len(arrival)):
            while server and server[0][0] <= arrival[i]:
                _, index = heapq.heappop(server)
                free.add(index)

            pos_i = i % k
            if pos_i not in free:
                temp_i = free.bisect_right(pos_i)
                if temp_i == len(free):
                    if not free:
                        continue
                    pos_i = free[0]
                else:
                    pos_i = free[temp_i]

            free.remove(pos_i)
            count[pos_i] += 1
            heapq.heappush(server, (arrival[i] + load[i], pos_i))

        maxi = max(count)
        res = [i for i in range(k) if count[i] == maxi]
        return res

# class Solution:
#     def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
#         count = [(0, i) for i in range(k)]
#         curr = [0 for _ in range(k)]
#         n = len(arrival)
#
#         def assign(i, j):
#             if curr[j]<= arrival[i]:
#                 curr[j] = arrival[i]+load[i]
#                 count[j] = (count[j][0]-1, count[j][1])
#                 return True
#             return False
#
#         for i in range(n):
#             if assign(i, i%k):
#                 continue
#             else:
#                 if curr[(i%k)+1:] and min(curr[(i%k)+1:])<= arrival[i]:
#                     for j in range((i%k)+1, k):
#                         if assign(i, j):
#                             break
#                 elif curr[:i%k] and min(curr[:i%k])<= arrival[i]:
#                     for j in range(0, i%k):
#                         if assign(i, j):
#                             break
#         heapq.heapify(count)
#         maxi = count[0][0]
#         res = []
#         while count and count[0][0] == maxi:
#             val, index = heapq.heappop(count)
#             res.append(index)
#         return res

# class Solution:
#     def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
#         count = [0 for _ in range(k)]
#         curr = [0 for _ in range(k)]
#         n = len(arrival)
#
#         def assign(i, j):
#             if curr[j]<= arrival[i]:
#                 curr[j] = arrival[i]+load[i]
#                 count[j]+=1
#                 return True
#             return False
#
#         for i in range(n):
#             if assign(i, i%k):
#                 continue
#             else:
#                 flag = True
#                 for j in range((i%k)+1, k):
#                     if assign(i, j):
#                         flag = False
#                         break
#                 if flag:
#                     for j in range(0, i%k):
#                         if assign(i, j):
#                             break
#         maxi = max(count)
#         res = []
#         for i, val in enumerate(count):
#             if val == maxi:
#                 res.append(i)
#         return res

print(Solution().busiestServers(3, [1,2,3,4,5], [5,2,3,3,3]))