class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordero = defaultdict(int)
        for i in range(26):
            ordero[order[i]] = i+1
        print(ordero)
        class MyStrOrder:
            def __init__(self, inner):
                self.inner = inner

            def __lt__(self, other):
                for i in range(min(len(self.inner), len(other.inner))):
                    a = ordero.get(self.inner[i])
                    b = ordero.get(other.inner[i])
                    if a != b:
                        return a < b
                return len(self.inner) < len(other.inner)
        '''stop = -1
        for i in range(len(words[0])):
            for j in range(len(words)):
                print(words[j])
                if(i == stop):
                    return True
                if(i == len(words[j]) - 1):
                    stop = len(words[j])
                if j == 0:
                    prev = words[j][i]
                    print(ordero[prev])
                else:
                    print(ordero[words[j][i]])
                    if ordero[prev] < ordero[words[j][i]]:
                        return True
                    elif ordero[prev] > ordero[words[j][i]]:
                        return False'''

        nonordero = words.copy()
        print(words)
        print(nonordero)
        words.sort(key = MyStrOrder)
        for i in range(len(words)):
            if nonordero[i] != words[i]:
                return False
        return True