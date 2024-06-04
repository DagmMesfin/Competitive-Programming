class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                cur.children[chrcode] = TrieNode()
            cur = cur.children[chrcode]
        cur.is_end = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                return False
            cur = cur.children[chrcode]
        return cur.is_end or not cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                return False
            cur = cur.children[chrcode]
        return True


