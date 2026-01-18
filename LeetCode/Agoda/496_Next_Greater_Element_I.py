from header import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = {}
        res = []
        num1_set = set(nums1)
        None_list = []
        for num in nums2:
            if num in num1_set:
                None_list.append(num)
            temp = []
            for item in None_list:
                if num>item:
                    di[item]=num
                else:
                    temp.append(item)
            None_list = temp

        for num in nums1:
            if num not in di:
                res.append(-1)
            else:
                res.append(di[num])
        return res

print(Solution().nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]))