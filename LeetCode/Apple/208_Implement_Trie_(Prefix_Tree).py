class TrieNode:

    def __init__(self):
        self.children = {}
        self.isword = False


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                newnode = TrieNode()
                node.children[c] = newnode
                node = newnode
            else:
                node = node.children[c]
        node.isword = True

    def search(self, word: str) -> bool:

        def dfs(curr, word):
            if len(word) == 1:
                if word in curr.children and curr.children[word].isword:
                    return True
                return False
            else:
                if word[0] in curr.children:
                    return dfs(curr.children[word[0]], word[1:])
                else:
                    return False

        return dfs(self.head, word)

    def startsWith(self, prefix: str) -> bool:
        def dfs(curr, word):
            if len(word) == 1:
                if word in curr.children:
                    return True
                return False
            else:
                if word[0] in curr.children:
                    return dfs(curr.children[word[0]], word[1:])
                else:
                    return False

        return dfs(self.head, prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

a = ["Trie","insert","search","search","startsWith","insert","search"]
b = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

obj = Trie()

for func, args in zip(a[1:], b[1:]):
    print(getattr(obj, func)(*args))