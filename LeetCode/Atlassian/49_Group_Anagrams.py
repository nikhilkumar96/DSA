from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dict = {}
        res = []
        for s in strs:
            str_counter_un = Counter(s)
            str_counter = tuple(sorted(str_counter_un.items()))
            if str_counter in counter_dict:
                counter_dict[str_counter].append(s)
            else:
                counter_dict[str_counter] = [s]

        for value in counter_dict.values():
            res.append(value)
        return res



# a = ["eat","tea","tan","ate","nat","bat"]
# a = [""]
a=["a"]
print(Solution().groupAnagrams(a))

