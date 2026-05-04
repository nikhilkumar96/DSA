from header import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1+nums2
        temp.sort()
        mid = len(temp)//2
        return temp[mid] if len(temp)%2!=0 else (temp[mid]+temp[mid-1])/2

print(Solution().findMedianSortedArrays( nums1 = [1,2], nums2 = [3,4]))