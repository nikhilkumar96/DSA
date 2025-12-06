from header import *
class Solution:
    def compress(self, chars: List[str]) -> int:

        def calc_compress(i, c):
            count = 0
            while i < len(chars):
                if chars[i] == c:
                    count += 1
                    i += 1
                else:
                    break
            if count == 1:
                return i, c
            return i, c + str(count)

        index = 0
        res = []
        while index < len(chars):
            index, s = calc_compress(index, chars[index])
            res.extend(list(s))
        chars[:] = res
        return len(res)

print(Solution().compress(["a","a","b","b","c","c","c"]))
# print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))








