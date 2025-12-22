from header import *
def check_valid(speed, dist, hour):
    old_data = sum([math.ceil(i / speed) for i in dist[:-1]])
    if old_data + dist[-1] / speed <= hour:
        return True
    return False


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1:
            return -1
        if sum(dist) <= hour:
            return 1

        for i in range(math.ceil(sum(dist) / hour), max(dist) + 1):
            if check_valid(i, dist, hour):
                return i
        final_hour = hour - (len(dist) - 1)
        final_val = int(dist[-1]//final_hour)
        return final_val if check_valid(final_val, dist, hour) else final_val+1


print(Solution().minSpeedOnTime(dist = [1,1,100000], hour = 2.01))
