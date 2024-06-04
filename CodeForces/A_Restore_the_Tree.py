from collections import defaultdict, deque


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,m = dmsllinp(int)
    graph = defaultdict(list)
    indegree = defaultdict(int)
    res = [0]*n
    for i in range(n-1+m):
        u,v = dmsllinp(int)
        graph[u].append(v)
        indegree[v]+=1
    
    q = deque()

    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
    
    while q:
        for _ in range(len(q)):
            valo = q.popleft()
            for neigh in graph[valo]:
                res[neigh-1] = valo
                indegree[neigh]-=1
                if not indegree[neigh]:
                    q.append(neigh)
    
    return res



    
    
    
    
    
    


for _ in range(1):
    for a in solve():
        print(a)