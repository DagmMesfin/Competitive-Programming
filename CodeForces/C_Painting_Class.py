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
    edges = dmsllinp(int)
    target_col = dmsllinp(int)
    init_col = [0]*n
    graph = defaultdict(list)
    for i in range(n-1):
        graph[i+2].append((edges[i],target_col[i+1]))
        graph[edges[i]].append((i+2,target_col[edges[i]-1]))
    colored = set()
    colorednum = 1
    queue = deque([1])

    while queue:
        for i in range(len(queue)):
            a = queue.popleft()
            if a not in colored and graph[a]:
                colored.add(a)
                for node,prevcol in graph[a]:
                    if node not in colored:
                        if target_col[node-1] != prevcol:
                            colorednum+=1
                        queue.append(node)
    return colorednum
                        
                        




for _ in range(1):
    print(solve())