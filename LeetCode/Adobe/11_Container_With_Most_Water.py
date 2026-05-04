from header import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height)-1
        maxarea = 0
        while l<r:
            curr_area = min(height[l],height[r])*(r-l)
            if curr_area>maxarea:
                maxarea = curr_area
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return maxarea

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))