from header import *

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        def move(li):
            i = 0
            temp = []
            c = 0
            p = 0
            while i < len(li):
                if li[i] == '#':
                    c += 1
                elif li[i] == '.':
                    p += 1
                else:
                    if c or p:
                        temp += ['.'] * p + ['#'] * c
                    temp.append('*')
                    c, p = 0, 0
                i += 1

            if c or p:
                temp += ['.'] * p + ['#'] * c
            return temp

        for i in range(len(boxGrid)):
            boxGrid[i] = move(boxGrid[i])
        return list(zip(*boxGrid[::-1]))


print(Solution().rotateTheBox([["#",".","*","."],["#","#","*","."]]))