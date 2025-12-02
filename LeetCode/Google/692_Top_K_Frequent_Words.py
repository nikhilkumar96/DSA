from header import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        fin_dict = SortedDict()
        for key, v in count.items():
            if v in fin_dict:
                fin_dict[v].append(key)
            else:
                fin_dict[v] = [key]

        res = []
        c = k
        for key in fin_dict.keys()[::-1]:
            if len(fin_dict[key]) > 1:
                fin_dict[key] = sorted(fin_dict[key])
            if len(fin_dict[key]) <= c:
                res.extend(fin_dict[key])
                c = k - len(res)
            else:
                res.extend(fin_dict[key][:c])
                break
        return res


print(Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))