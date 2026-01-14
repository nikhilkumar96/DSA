from header import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c_s1 = Counter(s1)
        m = len(s1)
        n = len(s2)
        i=0
        c_s2 = Counter(s2[0:0+m-1])
        while i+m<n+1:
            if s2[i+m-1] in c_s2:
                c_s2[s2[i+m-1]]+=1
            else:
                c_s2[s2[i+m-1]]=1
            if c_s2 == c_s1:
                return True
            c_s2[s2[i]]-=1
            i+=1
        return False

print(Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo"))