class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        maxlen = 0
        for c in s:
            if c not in subs:
                subs.append(c)
            else:
                while c in subs:
                    subs.pop(0)
                subs.append(c)
            maxlen = max(maxlen, len(subs))
        return maxlen


print(Solution().lengthOfLongestSubstring("abcabcbb"))