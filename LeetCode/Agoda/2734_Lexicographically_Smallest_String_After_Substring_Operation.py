
class Solution:
    def smallestString(self, s: str) -> str:
        check_all = []
        for c in s:
            if c == 'a':
                check_all.append(True)
            else:
                check_all.append(False)
        if all(check_all):
            return "".join(s[:-1]) + 'z'
        res = []
        flag = False
        for i, c in enumerate(s):
            if c != 'a':
                res.append(chr(ord(c) - 1))
                flag = True
            else:
                if flag:
                    res += s[i:]
                    break
                res.append(c)
        return ''.join(res)

print(Solution().smallestString("cbabc"))