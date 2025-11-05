class Trie:

    def __init__(self):
        self.children = {}
        self.isword = False


class WordDictionary:

    def __init__(self):
        self.head = Trie()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                newnode = Trie()
                node.children[c] = newnode
                node = newnode
            else:
                node = node.children[c]
        node.isword = True

    def search(self, word: str) -> bool:

        def dfs(curr, word):
            if len(word)==1:
                if (word=="." and any([curr.children[child].isword for child in curr.children])) or (word in curr.children and curr.children[word].isword):
                    return True
                return False
            else:
                if word[0] in curr.children.keys():
                    return dfs(curr.children[word[0]], word[1:])
                elif word[0] == ".":
                    flag = False
                    for child in curr.children:
                        flag = flag or dfs(curr.children[child], word[1:])
                    return flag
            return False


        return dfs(self.head, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# a = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# b = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
a = ["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
b = [[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]

obj = WordDictionary()

for name, args in zip(a[1:], b[1:]):
    print(getattr(obj, name)(*args))