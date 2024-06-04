import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                cur.children[chrcode] = TrieNode()
            cur.count+=1
            cur = cur.children[chrcode]
            
        cur.is_end = True
        cur.count+=1


        
    def search(self, word: str) -> bool:
        cur = self.root
        com = 0
        k = 0
        for i in range(len(word)):
            char = word[i]
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                return com+cur.count
            if k != 0:
                com+=cur.count
            else:
                k+=1
            cur = cur.children[chrcode]

        return com+cur.count

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            chrcode = ord(char) - ord("a")
            if not cur.children[chrcode]:
                return False
            cur = cur.children[chrcode]
        return True

def solve():
    trie = Trie()
    n = dmslinp(int)
    arro = []
    sumo = 0
    common_counto = 0
    for _ in range(n):
        elem = dmslinp()
        sumo+=len(elem)
        arro.append(elem)
        trie.insert(elem[::-1])
    
    for i in range(n):
        common_counto += trie.search(arro[i])

    return (2*n*sumo) - (2 * common_counto)
    

    

for _ in range(1):
    print(solve())