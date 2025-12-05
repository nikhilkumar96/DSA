from header import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for chars in zip(*strs):  # pairs of chars at same index
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break
        return ''.join(prefix)


print(Solution().longestCommonPrefix(["flower","flow","flight"]))