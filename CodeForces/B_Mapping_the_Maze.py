from collections import defaultdict


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
    counto = defaultdict(int)
    

    for i in range(m):
        u,v = dmsllinp(int)
        graph[u].append(v)
        graph[v].append(u)
    
    for k,v in graph.items():
        counto[len(v)]+=1
        
    print(counto)
    if counto[1] == 2 and counto[2] == n-2:
        return "bus topology"
    if counto[2] == n:
        return "ring topology"
    if counto[1] == n-1:
        return "star topology"
    return "unknown topology"
    
    


for _ in range(1):
    print(solve())