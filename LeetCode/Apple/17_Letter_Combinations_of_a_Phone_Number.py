from header import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        digit = list(digits)

        queue = []

        for i in digit:
            queue.append(letters[i])

        while len(queue) > 1:
            a = queue.pop(0)
            b = queue.pop(0)
            temp = []
            for i in a:
                for j in b:
                    temp.append(i + j)
            queue.insert(0, temp)
        return queue[0]

print(Solution().letterCombinations('23'))