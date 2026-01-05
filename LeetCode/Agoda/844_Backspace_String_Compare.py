from header import *


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def compile_string(temp):
            new_temp = ''
            i = len(temp) - 1
            c = 0
            while i >= 0:
                if temp[i] == "#":
                    c+=1
                elif c:
                    c-=1
                else:
                    new_temp += temp[i]
                i -= 1
            return ''.join(new_temp[::-1])

        if compile_string(s) == compile_string(t):
            return True
        return False


print(Solution().backspaceCompare(s = "ab##", t = "c#d#"))