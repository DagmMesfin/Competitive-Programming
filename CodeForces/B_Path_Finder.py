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
    graph = defaultdict(list)

    for _ in range(n-1):
        u,v,w = dmsllinp(int)
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    dist = [0]*n
    visited = set()
    queue = deque([0])
    while queue:
        for i in range(len(queue)):
            a = queue.popleft()
            if a not in visited and graph[a]:
                visited.add(a)
                for node,weight in graph[a]:
                    if node not in visited:
                        dist[node]+=weight+dist[a]
                        queue.append(node)
    return max(dist)


        


for _ in range(1):
    print(solve())