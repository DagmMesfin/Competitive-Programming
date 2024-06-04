class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(0,1) ]


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

from collections import Counter
import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))






import sys
import threading


def main():
    n = int(sys.stdin.readline().strip())
    trie = Trie()
    def solve():
        n = dmslinp(int)
        arr = dmsllinp(int)
        arr.sort()
        counto = Counter(arr)
        st_m = 0
        for numo,coun in counto.items():
            if coun >= 2**(numo + st_m):
                return "NO"
            else:
                st_m = 2**(numo + st_m) - counto
        def dfs(i,cur):
            cur = trie.root
            for k in [0,1]:
                dfs()

        return "YES"
        
    
    print(solve())





testcase = 0
T = int(input()) if testcase else 1
for _ in range(T):
    if __name__ == 'main':    
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
