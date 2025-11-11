import collections
from typing import List
from functools import reduce

class Solution(object):
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

# class Trie:
#
#     def __init__(self):
#         self.children = {}
#         self.isword = False
#
# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         self.head = Trie()
#
#         words.sort(key = len, reverse=True)
#         count_end = 0
#         for word in words:
#             node = self.head
#             flag = False
#             for i in word[::-1]:
#                 if i not in node.children:
#                     flag = True
#                     newnode = Trie()
#                     node.children[i] = newnode
#                     node = newnode
#                 else:
#                     node = node.children[i]
#             if flag:
#                 count_end += len(word)
#                 count_end+=1
#                 flag = False
#         return count_end




print(Solution().minimumLengthEncoding(["time", "me", "bell"]))