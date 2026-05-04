import copy

from header import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        maxLen = len(s)
        res = ""
        l=0
        r= 0
        di = deepcopy(count)
        for k in count.keys():
            di[k] = 0
        while r<len(s):
            if s[r] in di:
                di[s[r]]+=1
            while di>=count:
                if r-l<maxLen:
                    res = s[l:r+1]
                    maxLen = len(res)
                if s[l] in di:
                    di[s[l]]-=1
                l+=1
            r+=1
        return res



# print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution().minWindow(s = "cabwefgewcwaefgcf", t = "cae"))