from collections import defaultdict, deque

def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    words = []

    for _ in range(n):
        words.append(dmslsplit(input() , str))
    
    maxi = len(max(words , key=len))

    def check(word , i):
        return len(word) > i


    graph=  defaultdict(list)
    indegree = defaultdict(int)
    def compare(word1 , word2):
        i = 0
        while check(word1 , i) and check(word2 , i) and word1[i] == word2[i]:
            i += 1

        if check(word1 , i) and check(word2 , i):
            graph[word1[i]].append(word2[i])
            indegree[word2[i]] += 1
            return True

        return False
    
    for i in range(1 , n):
        if not compare(words[i-1] , words[i]) and len(words[i-1] ) > len(words[i]):
            print("Impossible")
            return
    


    alpha = []   

    def topSort():
        que = deque()
        order = []
        for i in range(97 , 97+26):
            if indegree[chr(i)] == 0:
                que.append(chr(i))

        while que:
            node = que.popleft()

            order.append(node)

            for nbr in graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    que.append(nbr)
        
        return order
        
    


    ans = topSort()
    if  len(ans) != 26:
        print("Impossible")
        return

    print("".join(ans))
    

testcase = 0
T = dmslinp(int) if testcase else 1
for _ in range(T):
    solve()