from collections import deque
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxnum = 0
        left = deque()
        for h in height:
            if h>maxnum:
                maxnum=h
            left.append(max(h, maxnum))

        maxnum=0
        right= deque()
        for h in height[::-1]:
            if h > maxnum:
                maxnum = h
            right.appendleft(max(h, maxnum))

        c=0
        for i in range(len(height)):
            c+=min(left[i],right[i])-height[i]
        return c

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))