from header import *

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score =0
        i=0
        n = len(instructions)
        visit = [False for _ in range(n)]
        while i>=0 and i <n:
            if visit[i]:
                break
            visit[i] = True
            if instructions[i] == "add":
                score+=values[i]
                i+=1
            else:
                i = i+values[i]
        return score

print(Solution().calculateScore(["jump","add","add","jump","add","jump"], [2,1,3,1,-2,-3]))