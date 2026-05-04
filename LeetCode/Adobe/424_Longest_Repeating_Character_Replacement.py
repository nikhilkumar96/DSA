from header import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        res=0
        max_di = 0
        curr_len = 0
        di = {}
        while r<len(s):
            if s[r] in di:
                di[s[r]]+=1
            else:
                di[s[r]]=1
            max_di = max(max_di,di[s[r]])
            curr_len+=1
            if curr_len-max_di>k:
                di[s[l]]-=1
                curr_len-=1
                l+=1
            r+=1
            res=max(res,curr_len)
        return res

print(Solution().characterReplacement(s = "AABABBA", k = 1))
