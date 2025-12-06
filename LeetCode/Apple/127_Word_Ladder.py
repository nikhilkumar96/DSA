from header import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 1
        queue = [beginWord]
        visited = set([beginWord])

        def word_alter(curr, word):
            diff = 0
            for i in range(len(curr)):
                if diff>1:
                    return False
                if curr[i] != word[i]:
                    diff+=1
            return True if diff ==1 else False

        while queue:
            curr_size = len(queue)

            for i in range(curr_size):
                curr = queue.pop(0)
                for word in wordList:
                    if word not in visited and word_alter(curr, word):
                        if word == endWord:
                            return count+1
                        visited.add(word)
                        queue.append(word)
            count+=1
        return 0

print(Solution().ladderLength(beginWord = "lost", endWord = "miss", wordList = ["most","mist","miss","lost","fist","fish"]))