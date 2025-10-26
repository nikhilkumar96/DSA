from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        chains = {}

        words = sorted(words, key=len)
        for word in words:

            chains[word] =1
            for i in range(len(word)):
                pre = word[:i]+word[i+1:]
                if pre in chains:
                    chains[word] = max(chains[word], chains[pre]+1)
        return max(chains.values())


a = ["a","b","ba","bca","bda","bdca"]

print(Solution().longestStrChain(a))