from header import *
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        bound = math.pow(2, 31)
        s = list(str(x))
        if '-' in s:
            s.remove('-')
            flag = True
        res = -int(''.join(s[::-1])) if flag else int(''.join(s[::-1]))
        return 0 if res < -bound or res > bound else res

print(Solution().reverse(123))
