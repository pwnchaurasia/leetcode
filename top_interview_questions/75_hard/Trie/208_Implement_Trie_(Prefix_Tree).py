class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children: return False
            cur = cur.children[w]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children: return False
            cur = cur.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)