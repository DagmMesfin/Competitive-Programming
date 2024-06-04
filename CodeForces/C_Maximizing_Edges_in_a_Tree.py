from collections import Counter, defaultdict, deque


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = int(input())
    graph = defaultdict(list)
    color = [0]*(n+1)
    

    for i in range(n-1):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node):
        stack = [node]
        while stack:
            indian = stack.pop()
            for i in list(graph[indian]):
                if not color[i]:
                    if color[indian] == 1:
                        color[i] = 2
                    else:
                        color[i] = 1
                    stack.append(i)
    for i in range(n+1):
        if not color[i]:
            dfs(i)

    return color.count(1) * color.count(2) - (n-1)



for _ in range(1):
    print(solve())