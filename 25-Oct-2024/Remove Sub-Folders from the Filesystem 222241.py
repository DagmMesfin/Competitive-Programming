# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> bool:
        cur = self.root
        isendo = False
        for char in word:
            chrcode = char
            if chrcode not in cur.children:
                cur.children[chrcode] = TrieNode()
            cur = cur.children[chrcode]
            if cur.is_end:
                isendo = True
        cur.is_end = True
        return isendo
        
    def search(self, word) -> bool:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            chrcode = char
            if chrcode not in cur.children:
                return False
            cur = cur.children[chrcode]
        return cur.is_end or not cur

    def startsWith(self, prefix) -> bool:
        cur = self.root
        for char in prefix:
            chrcode = char
            if chrcode not in cur.children:
                return False
            cur = cur.children[chrcode]
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        folder.sort(key = lambda l: len(l))
        ans = []

        for i in range(len(folder)):
            if not trie.insert(folder[i].split("/")):
                ans.append(folder[i])
        
        return ans



        