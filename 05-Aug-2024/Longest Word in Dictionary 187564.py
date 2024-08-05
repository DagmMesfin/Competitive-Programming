# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        cur.is_end = True
        for char in word:
            chrcode = ord(char) - ord("a")
            if not cur.child[chrcode]:
                cur.child[chrcode] = TrieNode()
            cur = cur.child[chrcode]
        cur.is_end = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            chrcode = ord(char) - ord("a")
            if not cur.is_end:
                return False
            cur = cur.child[chrcode]
        return word if cur.is_end else False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = defaultdict(list)
        maxo = 0
        for word in words:
            k = trie.search(word)
            if k:
                leno = len(k)
                maxo = max(maxo,leno)
                res[leno].append(k)
        res[maxo].sort()
        return res[maxo][0] if maxo else ""